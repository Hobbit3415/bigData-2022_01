### 1. Función aws Lambda que realiza descarga los sitios web en formato .txt

La función que se encarga de realizar la descarga de los sitios web es [scrapHeadlines.py](https://github.com/Hobbit3415/bigData-2022_01/blob/master/corte2/parcial02/scrapHeadlines/scrapHeadlines.py)

> Si se desea ejecutar, será necesario cambiar el nombre del bucket de destino

En el bucket de S3, la información se guardará con la siguiente estructura:
 > s3://bucket/headlines/raw/periodico=xxx/year=xxx/month=xxx/day=xxx

La información obtenida queda guardada en formato .txt (es guardada en crudo)
