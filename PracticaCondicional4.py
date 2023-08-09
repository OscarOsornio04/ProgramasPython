print("Programa de becas 2023")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print("Distancia a la escuela: " + str(distancia_escuela))

numero_hermanos = int(input("Introduce el numero de hermanos en el centro: "))
print("Numero de hermanos: " + str(numero_hermanos))

salario_familiar = int(input("Introduce el salario anual bruto: "))
print("Salario familiar: " + str(salario_familiar))

"""if distancia_escuela > 40 and numero_hermanos > 2 and salario_familiar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")"""

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
	print("Tienes derecho a beca")
else:
	print("No tienes derecho a beca")