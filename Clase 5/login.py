from flask import Flask, blueprints, render_template, request


logint= blueprints('logint', __name__)

@logint.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print(user, password)