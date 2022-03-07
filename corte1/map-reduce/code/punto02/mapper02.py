import sys
cont = 0

for line in sys.stdin:
	if cont == 0: 
		cont = 1
	else:
		print("Ingreso al mapper")
		precio = line.split(",")[1]
		ciudad = line.split(",")[7]
		print(ciudad, "\t", precio)
