def salario_total(sueldoH, horasTr, nombre):
	if(sueldoH >0 and sueldoH <=150):
		sueldoT = sueldoH * horasTr
		sueldoT = sueldoT - (sueldoT*0.05)
	elif(sueldoH >150 and sueldoH <300):
		sueldoT = sueldoH * horasTr
		sueldoT = sueldoT - (sueldoT*0.07)
	elif(sueldoH >300 and sueldoH <450):
		sueldoT = sueldoH * horasTr
		sueldoT = sueldoT - (sueldoT*0.09)

	print(f"{nombre} tu sueldo semanal es de {sueldoT}")
