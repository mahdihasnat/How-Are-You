####!/bin/bash

pushd howareyou

python manage.py makemigrations
python manage.py migrate

python manage.py runserver

popd