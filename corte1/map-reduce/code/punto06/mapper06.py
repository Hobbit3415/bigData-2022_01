import sys
input = sys.stdin
next(input)

for line in input:
	if not line:
		break
	condado = line.split(",")[8]
	ciudad = line.split(",")[6]
	print(condado, "\t", ciudad)
