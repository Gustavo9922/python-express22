#-*- Coding utf-8 -*-
#caracteres especiales


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])

def unida():
    return"Server Flask is running on port 5000!"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="localhost")
"""
0.0.0.0 es una direccion IP que permite que la aplicacion sea accesible desde cualquier direccion IP de la red local.
"""


