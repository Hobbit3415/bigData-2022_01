import sys

llave_actual = None
valor_actual = None
contador = 0

for line in sys.stdin:
	line = line.strip()
	key, val = line.split("\t")
	#key = int(key)
	val = int(val)
	if llave_actual == key:
		valor_actual += val
	else:
		if llave_actual:
			print(int(llave_actual), "\t", valor_actual)
		llave_actual = key
		valor_actual = val
print(int(llave_actual), "\t", valor_actual)