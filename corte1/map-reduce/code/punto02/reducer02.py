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
			print(llave, total)
			#cont = 0
		llave = lla
		total = val
print(cont)
total = total/cont
cont = 0
print(llave, total)
