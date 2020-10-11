#!/bin/bash
export FLASK_APP=.\src\main.py
source .\env\Scripts\activate
flask run -h 0.0.0.0