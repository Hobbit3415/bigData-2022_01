import sys
input = sys.stdin
next(input)

for line in input:
	if not line:
		break
	precio = line.split(",")[1]
	fecha = line.split(",")[2]
	year = fecha.split("-")[0]
	mes = fecha.split("-")[1]
	print(year, "\t",'%10d'%int(mes), "\t",1)
