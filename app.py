from pprint import pprint
from flask import Flask, jsonify
from database.connexion import IntelliquizzDB
from helpers.converters import Converters
import gspread
import json

import json

app = Flask(__name__)

@app.route("/")
def index():
    google_credentials = gspread.service_account(filename='credentials.json')
    sheet = google_credentials.open_by_key("1L6NurushGZT7vDXeR2v4kMYxxahkdhLkhdmLLROmECY")
    worksheet = sheet.worksheet("ICT")
    data = worksheet.get_all_records()
    return json.dumps(data)


@app.route("/<subject>/<level>/<number>/" )
def universal(subject,level,number):
    google_credentials = gspread.service_account(filename='credentials.json')
    sheet = google_credentials.open_by_key("1L6NurushGZT7vDXeR2v4kMYxxahkdhLkhdmLLROmECY")
    worksheet = sheet.worksheet(subject)
    questions = []
    
    data = worksheet.get_all_records()
    for question in data:
        if(question["subject"] == subject and question["level"] == level):
            questions.append(question)
            if(len(questions) == number):
                break
        
    return {"results": json.dumps(questions)}, 200