# CALCULADORA
import math
print("Bienvenido Ala Calculadora")
n1= int(input("Primer numero: "))
n2 = int(input("Segundo numero: "))

operacion = """

Que operación deseas realizar ?

1 - Suma
2 - Resta
3 - Multiplicación
4 - División
5 - División Entera

Elige una opción: """

opcion = int(input(operacion))

if opcion == 1:
    print(n1 + n2)
elif opcion == 2:
    print(n1 - n2)
elif opcion == 3:
    print(n1 * n2)
elif opcion == 4:
    print(n1 / n2)
elif opcion == 5:
    print(n1 // n2)
else:
    print("Opcion incorrecta")

print("Programa finalizado")
