from flask import Flask, request, jsonify
from cliente import buscar_cliente

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def cliente():
    datos = request.get_json()
    ci = datos.get("ci")
    respuesta = buscar_cliente(str(ci))
    return jsonify(respuesta)

if __name__ == '__main__':
    app.run(debug=True, port=5003, host="localhost")








