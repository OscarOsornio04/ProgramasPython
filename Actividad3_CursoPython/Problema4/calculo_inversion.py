def inversion(inversion_inicial):
	print(f"Inversion en 1961 ${inversion_inicial}")
	inversion =inversion_inicial
	for i in range(1961,2024):
		inversion = inversion + (inversion_inicial * 0.15)

	print(f"Inversion en 2023 ${inversion}")
