import sys

llave = None
total = 0
cont = 0

for line in sys.stdin:
	lla, val = line.split("\t")
	val = int(val)
	if lla == llave:
		total += val
	else:
		if llave is not None:
			print(total,"\t",llave)
		llave = lla
		total = val
print(total,"\t",llave)
