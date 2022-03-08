import sys

llaveCondado = None
llaveCiudad = None
cont = 0

for line in sys.stdin:
	llaCo, llaCi = line.split("\t")
	if llaCo == llaveCondado:
		if llaCi != llaveCiudad:
			cont += 1
	else:
		if llaveCiudad is not None:
			print(cont,"\t","1")
		llaveCiudad = llaCi
		llaveCondado = llaCo
		cont = 1
print(cont,"\t","1")
