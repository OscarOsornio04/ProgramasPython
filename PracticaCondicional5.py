print("Asiganturas optativas Año 2023")
print("Asiganturas optativas:\nInformatica grafica\nPruebas de software\nUsabilidad y accesibilidad")

#asignatura = input("Escoge la asignatura elegida: ")

opcion = input("Escoge la asignatura elegida: ")

asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida: " + asignatura)
else:
	print("La asignatura escogida no esta contemplada")