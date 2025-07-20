"""
Ejemplos estructura de control for
"""

#Ejemplo en C++
#for (int i = 0; i < 10; i++) {
#    cout << "el valor de i es: " << i << endl;
#}

#contador = 10
#for i in range(0, contador):
#    print("el valor de i es:", i)
#print("Fin del bucle for")

#Ejemplo con listas
array = ["futbol", "PC", 18.6, 18, [6, 7, 10.4], True, False]

for i in range(len(array)):
    print("el valor de i es:", i)
    print("el valor del elemento es:", array[i])
print("Fin del bucle for con listas")