#Ejercicio 1

"""print("Autobuses \"La Curva Loca\"")
print("Tarifa por 1 Km: $15\tPara un viaje sencillo (1km - 50km)\n")
kilometros_recorridos = int(input("Ingrese los Kilometros a recorrer: "))
if kilometros_recorridos > 0 and kilometros_recorridos < 50:
	costo = kilometros_recorridos * 15
	print(f"\nTendras que pagar ${costo} por {kilometros_recorridos} km a recorrer")
else:
	print("\nKilometraje incorrecto")"""


#Ejercicio 2

"""print("Costo de llamada: $12 por minuto\n")
minutos = int(input("Ingrese los minutos que duro su llamada: "))
costo_llamada = minutos * 12
print(f"Su llamada duro {minutos} minutos, por lo tanto son ${costo_llamada}")"""

#Ejercicio 3

"""print("\nPorcentajes de examenes:\nPrimer examen\t25%\nSegundo examen\t25%\nTercer examen\t50%\n")
calificacion_examen1 = float(input("Ingresa tu calificacion del primer examen (0-10): "))
calificacion_examen2 = float(input("Ingresa tu calificacion del segundo examen (0-10): "))
calificacion_examen3 = float(input("Ingresa tu calificacion del tercer examen (0-10): "))

promedio = (calificacion_examen1 * 0.25) + (calificacion_examen2 * 0.25) + (calificacion_examen3 * 0.5)

print(f"\nTu promedio es de {promedio}")"""

#Ejercicio 4

"""print("\nTarifa de estacionamiento:\nPrimeras dos horas\t$5.00 c/u\nSiguientes tres horas\t$4.00 c/u")
print("Cinco siguientes\t$3.00 c/u\nMas de diez horas\t$2.00 c/u\n")

horas = int(input("Total de horas: "))

if horas <= 2:
	costo = horas * 5
elif horas > 2 and horas <= 5:
	costo = horas * 4
elif horas > 5 and horas <= 10:
	costo = horas * 3
else:
	costo = horas * 2

print(f"Usted pagara ${costo} por {horas} horas")"""

#Ejercicio 5

"""salario = 1500
print(f"\nSalario inicial: ${salario}\n")
for i in [1,2,3,4,5,6]:
	salario = (salario*0.1) + salario
	print(f"Salario en el {i} año: ${salario}")

print(f"\nSalario despues de 6 años: ${salario}")"""

#Autor: Oscar Osornio Sanchez

