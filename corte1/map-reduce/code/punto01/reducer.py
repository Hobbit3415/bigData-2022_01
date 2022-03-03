import sys

llave = None
total = 0

for line in sys.stdin:
	lla, val = line.split("\t")
	val = int(val)
	if lla == llave:
		total += val
	else:
		if llave is not None:
			print(llave, total)
		llave = lla
		total = val
print(llave, total)
