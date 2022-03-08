import sys

llaveAnio = None
maxValor = 0
maxMes = 0

for line in sys.stdin:
	llaanio, llames, val = line.split("\t")
	val = int(val)
	if llaanio == llaveAnio:
		if maxValor < val:
			maxValor = val
			maxMes = llames
	else:
		if llaveAnio is not None:
			print(llaveAnio,"\t",maxMes)
		llaveAnio = llaanio
		maxValor = val
		maxMes = llames
print(llaveAnio,"\t",maxMes)
