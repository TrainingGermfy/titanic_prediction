#!/bin/bash
echo """
runtime: python39
entrypoint: gunicorn -b :$PORT main:app
env_variables:
  GOOGLE_PROJECT_ID: \"$GOOGLE_PROJECT_ID"
"""