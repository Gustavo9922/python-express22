#-*- Coding utf-8 -*-
#caracteres especiales


from flask import Flask, jsonify, request
from login import logint
from logout import logout


app = Flask(__name__)

##Se expone el blueprint de login
app.register_blueprint(logint)
app.register_blueprint(logout)
@app.route('/', methods=['GET'])

def unida():
    return"Server Flask is running on port 5000!"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="localhost")
"""
0.0.0.0 es una direccion IP que permite que la aplicacion sea accesible desde cualquier direccion IP de la red local.
"""


