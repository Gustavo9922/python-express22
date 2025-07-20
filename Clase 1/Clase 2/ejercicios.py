"""
Crear un programa que pida dos numeros
y obtenga como resultado cual de ellos es par
o si ambos lo son.
#Si ambos son pares, mostrar el mensaje  "Ambos numeros son pares"
#Si uno es par y otro impar, mostrar el mensaje "Uno es par y otro impar"

"""
# Números
num1 = 8
num2 = 3

# Verificar si son pares o impares
es_par1 = num1 % 2 == 0
es_par2 = num2 % 2 == 0

# Lógica de decisión
if es_par1 and es_par2:
    print("Ambos números son pares")
elif es_par1 or es_par2:
    print("Uno es par y otro impar")
else:
    print("Ambos números son impares")