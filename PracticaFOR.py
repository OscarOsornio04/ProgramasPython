"""for i in [1,2,3]:
	print("Hola")

for i in ["primavera", "verano", "otoño", "invierno"]:
	print("Hola")"""

#for i in ["Pildoras","Informaticas",3]:
#	print("Hola", end ="")

#for i in "juan@pildorasinformaticas.es":
#	print("Hola", end = " ")

"""email = False

for i in "juan@pildorasinformaticas.es":
	if (i == "@"):
		email = True
if email == True:
	print("Email correcto")
else:
	print("El email no es correcto")"""

#mi_email = input("Ingrese su direccion de email: ")
#email = False
#contador = 0

"""for i in mi_email:
	if (i == "@"):
		email = True
if email == True:
	print("Email correcto")
else:
	print("El email no es correcto")"""

"""for i in mi_email:
	if (i == "@" or i == "."):
		contador = contador + 1
if contador == 2:
	print("Email correcto")
else:
	print("El email no es correcto")"""


"""for i in range(5,50,3):
	print(f"Valor de la variable {i}")"""

valido = False 

email = input("Introduce tu email: ")

for i in range(len(email)):
	if email[i] == "@":
		valido = True

if valido:
	print("Email correcto")
else:
	print("Email incorrecto")

