"""
Ejemplos de listas en Python
"""

array = ["futbolt", "PC", 18.6, 18, [6,7,10.4], True, False]

print(array)

#Acceso a los elementos de la lista
print(array[0])
print(array[4])
print(array[0:3])
print(len(array))  # Longitud de la lista
array.append("66")  # Añadir un elemento al final de la lista
print(array)
array.insert(2, "balocento")  # Insertar un elemento en una posición específica
print(array)
array.extend(["tenis", "natacion"])  # Añadir varios elementos al final de la lista
print(array)
array.remove("PC")  # Eliminar un elemento específico
print(array)
array.pop()  # Eliminar el último elemento de la lista
print(array)
array.pop(2)  # Eliminar un elemento en una posición específica
print(array)
array.clear()  # Limpiar la lista
print(array)
array= ["futbol", "PC", 18.6, 18, [6,7,10.4], True, False]
array2=["baloncesto","tenis", "natacion"]
array3=array+array2  # Concatenar dos listas
print(array3)
print("futbol" in array3)
print(array3.index("baloncesto"))
print(array3.count("natacion"))  # Contar cuántas veces aparece un elemento
array4=[1,2,3,4,5,6,7,8,9,10]
array4.reverse()  # Invertir el orden de los elementos
print(array4)
array5=[1,2,3,4,5,6,7,8,9,10]
array5.sort()  # Ordenar la lista
print(array5)

