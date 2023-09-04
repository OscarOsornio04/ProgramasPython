def calculo_cubo(total_numeros):
	for i in range(0, total_numeros):
		numero_natural = int(input("Ingrese un numero natural: "))
		if(numero_natural > 0):
			print(f"{i+1}.- El cubo del numero {numero_natural} es {numero_natural**3}")
		else:
			print(f"El numero {numero_natural} no es un numero natural")