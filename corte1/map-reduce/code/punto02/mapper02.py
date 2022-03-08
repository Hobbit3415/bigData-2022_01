import sys
input = sys.stdin
next(input)

for line in input:
	if not line:
		break
	precio = line.split(",")[1]
	ciudad = line.split(",")[6]
	print(ciudad, "\t", precio)
