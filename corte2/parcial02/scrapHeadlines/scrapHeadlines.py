import boto3
import requests
from datetime import datetime

# Links de los sitios web
urlBbc = 'https://www.bbc.com/'
urlJournal = 'https://www.nejm.org/'
# Crea un cliente de S3
s3 = boto3.client('s3')
# Toma la fecha y la hora de ya
# (osea, en el momento en el que se llama al metodo)
now = datetime.now()
# strftime extrae lo que se le pida del objeto 'hoy'

# Las siguientes 3 variables, son string
# el argumento '%Y' da formato al año
year = now.strftime("%Y")
# el argumento '%m' da formato al mes
month = now.strftime("%m")
# el argumento '%d' da fotmato al dia
day = now.strftime("%d")

nombreBucket = 'parcial02'
# Primera parte del path para el nombre de los periodicos
directorio = 'headlines/raw/periodico='
# segunda parte del path para las fechas y demas
path = 'year='+year+'/month='+month+'/day='+day

def handler(event, context):

        # Solicita la pagina de la bbc y del journal
        pageBbc = requests.get(urlBbc)
        pageJournal = requests.get(urlJournal)

        # Parsea el contenido de los sitios como texto
        txtBbc = pageBbc.text
        txtJournal = pageJournal.text
        # Coloca en un bucket de S3 el texto parseado de cada uno de los sitios web en su
        # respectivo Path que se ve asi:
                # Key = 'headlines/raw/periodico=bbc/year=2022/month=04/day=30/rawBbc.txt'
        s3.put_object(Bucket=nombreBucket, Body=txtBbc , Key=directorio+"bbc/"+path+"/rawBbc.txt")
        s3.put_object(Bucket=nombreBucket, Body=txtJournal , Key=directorio+"journal/"+path+"/rawJournal.txt")
        return {}
