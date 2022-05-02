# Parcial 02 - Web Scraping
# Por: Valentina Del Pilar Franco y Emmanuel Mora Mosquera
# Universidad Sergio Arboleda

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

El script con el que se realizó la tabla es el siguiente:
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
Tras la creación de la tabla, es posible realizar consultas a esta mediante el catalogo de presto-cli. Consultas cómo:
```
presto:default> select * from news where periodico='journal';
```
Cuyo resultado es:
```
                         titular                         |      categoria       |                         url
---------------------------------------------------------+----------------------+-----------------------------------------------------
 CT or Coronary Angiography in Stable Chest Pain         | Original Article     | /doi/full/10.1056/NEJMoa2200963?query=featured_home
 Communicating Covid-19 Science                          | Editorial            | /doi/full/10.1056/NEJMe2205606?query=featured_home
 "Peers                                                  |  Professionalism     |  and Improvement"
 A Data Infrastructure for Clinical Trial Diversity      | Perspective          | /doi/full/10.1056/NEJMp2201433?query=featured_home
 Expanding Accountable Care among Medicare Beneficiaries | Perspective          | /doi/full/10.1056/NEJMp2202991?query=featured_home
 The E-Cigarette Flavor Debate                           | Perspective          | /doi/full/10.1056/NEJMp2119107?query=featured_home
 Needlestick                                             | Perspective          | /doi/full/10.1056/NEJMp2201012?query=featured_home
 Protection against Omicron by a Fourth Vaccine Dose     | Original Article     | /doi/full/10.1056/NEJMoa2201688?query=featured_home
 Vaccine for RSV in Pregnancy                            | Original Article     | /doi/full/10.1056/NEJMoa2106062?query=featured_home
 Nasal High-Flow Therapy during Neonatal Intubation      | Original Article     | /doi/full/10.1056/NEJMoa2116735?query=featured_home
 Ipilimumab after Anti–PD-1 and Anti–LAG-3 Therapy       | Correspondence       | /doi/full/10.1056/NEJMc2119768?query=featured_home
 Restricted Calories and Eating Times in Weight Loss     | Original Article     | /doi/full/10.1056/NEJMoa2114833?query=featured_home
 Understanding Vaccine Safety                            | Review Article       | /doi/full/10.1056/NEJMra2200583?query=featured_home
 Early-Onset Colorectal Cancer                           | Review Article       | /doi/full/10.1056/NEJMra2200869?query=featured_home
 Metric Myopia                                           | Medicine and Society | /doi/full/10.1056/NEJMms2200977?query=featured_home
 "A Man with Myalgias                                    |  Fever               |  and Bradycardia"
 Reassessing Quality Assessment                          | Medicine and Society | /doi/full/10.1056/NEJMms2200976?query=featured_home
(17 rows)

Query 20220502_041152_00008_x8atd, FINISHED, 2 nodes
Splits: 17 total, 17 done (100.00%)
1:16 [17 rows, 1.82KB] [0 rows/s, 24B/s]
```
Aqui tenemos un segundo ejemplo:
```
presto:default> select categoria from news where periodico='journal';
      categoria
----------------------
 Original Article
 Editorial
  Professionalism
 Perspective
 Perspective
 Perspective
 Perspective
 Original Article
 Original Article
 Original Article
 Correspondence
 Original Article
 Review Article
 Review Article
 Medicine and Society
  Fever
 Medicine and Society
(17 rows)

Query 20220502_041921_00015_x8atd, FINISHED, 1 node
Splits: 17 total, 17 done (100.00%)
0:01 [17 rows, 1.82KB] [11 rows/s, 1.23KB/s]
```
