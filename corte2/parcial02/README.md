### 1. Función aws Lambda que realiza scraping los sitios web en formato .txt

La función que se encarga de realizar la descarga de los sitios web es [scrapHeadlines.py](https://github.com/Hobbit3415/bigData-2022_01/blob/master/corte2/parcial02/scrapHeadlines/scrapHeadlines.py)

> Si se desea ejecutar, será necesario cambiar el nombre del bucket de destino

En el bucket de S3, la información se guardará con la siguiente estructura:
 > s3://bucket/headlines/raw/periodico=xxx/year=xxx/month=xxx/day=xxx

La información obtenida queda guardada en formato .txt (es guardada en crudo)

### 2. Función aws Lambda procesa los archivos .txt anteriores y extrae los titulares, las categorias y los enlaces de cada noticia

La función que se encarga de procesar la información de los sitios web es [scrapNewsFinal.py](https://github.com/Hobbit3415/bigData-2022_01/blob/master/corte2/parcial02/scrapNewsFinal/scrapNewsFinal.py).

Esta función, luego de extraer los datos, los convierte en un archivo .csv

Posteriormente, este archivo se sube a un bucket en S3 con la siguiente estructura:
> s3://bucket/news/final/periodico=xxx/year=xxx/month=xxx/day=xxx

Tras realizar este procesamiento, mediante el catalogo de HIVE, se creó una tabla externa llamada "news", la cual contiene toda la información previa.

El scrip con el que se realizó la tabla es el siguiente:
```
CREATE EXTERNAL TABLE news(
	titular string,
	categoria string,
	url string
	)
	PARTITIONED BY (periodico string, year int, month int, day int)
	ROW FORMAT DELIMITED
	fields terminated by ","
	escaped by "\\"
	lines terminated by "\n"
	location "s3://parcial02/news/final/"
	TBLPROPERTIES ("skip.header.line.count"="1");
```
