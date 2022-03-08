import sys

llave = None
mes = 0
total = 0

for line in sys.stdin:
	lla, mon, val = line.split("\t")
	val = int(val)
	mon = int(mon)
	if lla == llave and mes == mon:
		total += val
	else:
		if (llave and mes) is not None:
			print(llave,"\t",mes,"\t",total)
		llave = lla
		total = val
		mes = mon

print(llave,"\t",mes,"\t",total)
