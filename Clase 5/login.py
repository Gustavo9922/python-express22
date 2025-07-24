from flask import Blueprint, blueprints, Flask, jsonify, request


logint= Blueprint('logint', __name__)

@logint.route('/login', methods=['POST'])

def llamarServicioSet():
    user= request.json.get('user')
    password= request.json.get('password')
    print("User enviado: ",user, "Pass enviado", password)

    codRes, menRes, accion, rol, user = inicializarVariables(user, password)

    salida = {
        "codRes": codRes,
        "menRes": menRes,
        "usuario": user,
        "accion": accion,
        "rol": rol # type: ignore
    }

    return jsonify(salida)



def inicializarVariables(user, password):
    codRes = "SIN_ERROR"
    menRes = "OK"
    accion = "Login exitoso"
    rol="Admin"
    userLocal = "gustavo"
    passwordLocal = "123456"

    try:
        if user == userLocal and password == passwordLocal:
            print("Login exitoso")
            accion = "Login exitoso"
        else:
            codRes = "ERROR"
            menRes = "Usuario o contraseña incorrectos"
            accion = "Login fallido"
            rol = "N/A"
            user = "N/A"
            return codRes, menRes, accion, rol, user
    except Exception as e:
        print("Error en el login:", e)
        codRes = "ERROR"
        menRes = "Error en el login"
        accion = "Error en el login"
        rol = "N/A"
        user = "N/A"
        return codRes, menRes, accion, rol, user

    return codRes, menRes, accion,rol




