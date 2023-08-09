print("Programa de evaluacion de notas de alumnos")

nota_alumno = input("Introduce la nota del alumno: ") #Con input se leen datos y cuando se pone texto en el parentesis se imprime eso primero

def evaluacion(nota):
	valoracion = "aprobado"
	if nota < 5:
		valoracion = "suspenso"
	return valoracion

print(evaluacion(int(nota_alumno)))