import sys
input = sys.stdin
next(input)

for line in input:
	if not line:
		break
	precio = line.split(",")[1]
	ciudad = line.split(",")[6]
	fecha = line.split(",")[2]
	year = fecha.split("-")[0]
	if ciudad == "STAMFORD" and year == "2015": 
		print(ciudad, "\t",'%10d'%int(precio), "\t",year)

