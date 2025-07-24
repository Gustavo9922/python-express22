clientes = {
    "5705785": {
        "nombre": "Gustavo David",
        "apellidos": "Araujo Roa"
    }
}

def buscar_cliente(ci):
    if ci in clientes:
        return {
            "accion": "Success",
            "codRes": "SIN_ERROR",
            "menRes": "OK",
            "ci": ci,
            "nombre": clientes[ci]["nombre"],
            "apellidos": clientes[ci]["apellidos"]
        }
    else:
        return {
            "accion": "Cliente no está en el sistema",
            "codRes": "ERROR",
            "menRes": "Error cliente",
            "ci": ci
        }
