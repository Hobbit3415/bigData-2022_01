import sys

llave = None
total = 0
cont = 0

for line in sys.stdin:
	lla, val = line.split("\t")
	val = int(val)
	if lla == llave:
		total += val
		cont = cont +  1
	else:
		if llave is not None:
			#total = total/cont
			print(llave, total/cont)
			#cont = 0
		llave = lla
		total = val
		cont = 1
print(llave, total/cont)
