import flask
from flask_cors import CORS
from joblib import load
from flask import request, jsonify

app = flask.Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
logreg = load('./titanic_logreg.joblib')


@app.route('/', methods=['POST'])
def home():
    # Age,SibSp,Parch,isfemale,Fare, Pclass_Second,Pclass_Third,Cabin_class_B,Cabin_class_C,Cabin_class_D,
    # Cabin_class_E,Cabin_class_F,Cabin_class_G,Cabin_class_T,Cabin_class_U,Embarked_Q,Embarked_S,Embarked_U

    # pasajero = {'Age':48, 'SibSp':1, 'Parch':2, 'Fare':150, 'isfemale':0, 'Pclass_First':0, 'Pclass_Second':1,
    #           'Pclass_Third':0, 'Cabin_class_A':1, 'Cabin_class_B':0, 'Cabin_class_C':0, 'Cabin_class_D':0,
    #           'Cabin_class_E': 0, 'Cabin_class_F': 0, 'Cabin_class_G': 0, 'Cabin_class_T': 0,
    #            'Cabin_class_U': 0, 'Embarked_C': 1, 'Embarked_Q': 0, 'Embarked_S': 0}
    data = request.get_json()
    form_edad = int(data['inpEdad'])
    form_sibSP = int(data['inpSibSp'])
    form_parch = int(data['inpParch'])
    form_fare = float(data['inpTarifa'])
    form_isfemale = int(data['inpGenero'])
    form_class = [0, 0]
    form_embarked = [0, 0, 0]
    form_cabin_class = [0, 0, 0, 0, 0, 0, 0, 0]
    if int(data['inpClase']) > 1:
        form_class[int(data['inpClase']) - 2] = 1
    if int(data['inpEmbarque']) > 1:
        form_embarked[int(data['inpEmbarque']) - 2] = 1
    if int(data['inpCabina']) > 1:
        form_cabin_class[int(data['inpCabina']) - 2] = 1

    pasajero = [[form_edad, form_sibSP, form_parch, form_fare, form_isfemale, form_class[0], form_class[1],
                 form_cabin_class[0], form_cabin_class[1], form_cabin_class[2], form_cabin_class[3], form_cabin_class[4],
                 form_cabin_class[5], form_cabin_class[6], form_cabin_class[7], form_embarked[0], form_embarked[1],
                 form_embarked[2]]]
    print(pasajero)
    y_prob = logreg.predict(pasajero)[0] == 1
    resultado = {'sobrevive': str(y_prob)}
    print(resultado)
    return jsonify(resultado)

if __name__ == '__main__':
    app.run()
