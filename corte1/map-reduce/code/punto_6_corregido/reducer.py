import sys

llave_actual = None
valor_actual = 0
llave_actual_2 = None

for line in sys.stdin:
	line = line.strip()
	key, val = line.split("\t")
	val = int(val)
	if llave_actual == key.split(",")[0]:
		if llave_actual_2 != key.split(",")[1] and llave_actual != llave_actual_2:
				valor_actual += val
				llave_actual_2 = key.split(",")[1]
	else:
		if llave_actual:
			print(llave_actual, "\t", valor_actual)	
		llave_actual = key.split(",")[0]
		llave_actual_2 = key.split(",")[1]
		valor_actual = val 
print(llave_actual, "\t", valor_actual)