#-*- Coding utf-8 -*-
#caracteres especiales


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def unida():
    return"hola desde la unida"
