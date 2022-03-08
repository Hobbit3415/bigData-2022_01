import sys

llave = None
minimo = 0

for line in sys.stdin:
	lla, val = line.split("\t")
	val = int(val)
	if lla == llave:
		if val < minimo:
			minimo = val
	else:
		if llave is not None:
			print(llave,"\t",minimo)
		llave = lla
		minimo = val
print(llave,"\t", minimo)
