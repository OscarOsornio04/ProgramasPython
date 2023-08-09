"""i=1
while i<=10:
	print(f"Ejecucion {i}")
	i=i+1
print("Termino la Ejecucion")

edad = int(input("Introduce tu edad porfavor: "))

while edad <0:
	print("Has introducido una edad negativa. Vuelve a intentarlo")
	edad = int(input("Introduce tu edad porfavor: "))

while edad <5 or edad>100:
	print("Has introducido una edad incorrecta. Vuelve a intentarlo")
	edad = int(input("Introduce tu edad porfavor: "))


print("Gracias por colaborar")
print(f"Edad del aspirante {edad}" )"""

import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero porfavor: "))

intentos = 0

while numero < 0:
	print("No se puede hallar la raiz de un numero negativo")

	if intentos == 2:
		print("Has consumido demasiados intentos. El programa ha finalizado")
		break

	numero = int(input("Introduce un numero porfavor: "))

	if  numero < 0:
		intentos = intentos + 1

if intentos < 2:
	solucion = math.sqrt(numero)
	print(f"La raiz cuadrada de {numero} es {solucion}")
