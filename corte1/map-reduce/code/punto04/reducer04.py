import sys
lista1 = []
lista2 = []
lista3 = []

for line in sys.stdin:
	lla, val, a = line.split("\t")
	val = int(val)
	a = int(a)
	lista1.append(lla)
	lista2.append(val)
	lista3.append(a)
	#print(lla,"\t",val,"\t",a)

lista2.sort()

for i in range(len(lista1)):
	print(lista1[i],"\t",lista2[i],"\t",lista3[i])
