import sys

arreglo = []
for line in sys.stdin:
	laimu = line.split()
	arreglo.append(laimu)

auxArr = []
for l in arreglo:
	auxArr.append(l)

for i in range(len(auxArr)):
	contador = 1
	for j in range(i+1, len(auxArr)):
		contador = contador +1
	print(auxArr[i], contador)
