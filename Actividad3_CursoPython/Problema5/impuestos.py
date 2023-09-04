def impuestos_autos(clave_auto, precio_auto):
	if clave_auto == 1:
		por_auto = 0.1
	elif clave_auto == 2:
		por_auto = 0.07
	elif clave_auto == 3:
		por_auto = 0.05
	impuesto = precio_auto * por_auto
	print(f"El costo del coche ${precio_auto} con clave {clave_auto} paga un impuesto de ${impuesto}")
