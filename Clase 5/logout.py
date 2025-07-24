from flask import Blueprint, blueprints, Flask, jsonify, request


logout= Blueprint('logint', __name__)

@logout.route('/logout', methods=['POST'])
def logout():
    user= request.json.get('user')
    password= request.json.get('password')
    print("User enviado: ", user, "Pass enviado", password)


