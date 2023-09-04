from calculos_salarios import salario_total

print("\nCalculo de salario semanal")
print("Solo pueden ser maximo 48 horas maximas (lunes a sabado)\n")
numero_trabajadores = int(input("Numero de trabajadores: "))

for i in range(0,numero_trabajadores):
	print(f"\nTrabajador {i+1}")
	nombre_trabajador = input("Ingresa tu nombre: ")
	horas_trabajadas = int(input("¿Cuantas horas trabajo?: "))
	sueldo_hora = int(input("¿Cual es tu sueldo por hora?: "))
	salario_total(sueldo_hora, horas_trabajadas, nombre_trabajador)
