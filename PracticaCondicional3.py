"""edad = 7

if 0 < edad < 100:
	print("Edad es correcta")
else:
	print("Edad incorrecta")"""

salario_presidente = int(input("Ingrese salario presidente >> "))
print("Salario del presidente = " + str(salario_presidente))

salario_director = int(input("Ingrese salario director >> "))
print("Salario del director = " + str(salario_director))

salario_jefe_area = int(input("Ingrese salario Jefe Area >> "))
print("Salario del Jefe de Area = " + str(salario_jefe_area))

salario_administrativo = int(input("Ingrese salario Administrativo >> "))
print("Salario del administrativo = " + str(salario_administrativo))

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")
