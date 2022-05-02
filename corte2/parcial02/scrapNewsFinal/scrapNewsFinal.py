import boto3
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup

nombreBucket = 'parcial02'
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

# Primera parte del path para el nombre de los periodicos
directorioRaw = 'headlines/raw/periodico='

directorioFinal = 'news/final/periodico='

# segunda parte del path para las fechas y demas
path = 'year='+year+'/month='+month+'/day='+day

def handler(event, context):

        # Solicita la pagina de la bbc y del journal
        s3.download_file(nombreBucket, directorioRaw+"bbc/"+path+"/rawBbc.txt", '/tmp/rawBbc.txt')
        s3.download_file(nombreBucket, directorioRaw+"journal/"+path+"/rawJournal.txt", '/tmp/rawJournal.txt')

        dfBbc = scrapBbc(open('/tmp/rawBbc.txt').read())
        dfEngland = scrapJournal(open('/tmp/rawJournal.txt').read())

        dfBbc.to_csv('/tmp/dfBbc.csv', index=None)
        dfEngland.to_csv('/tmp/dfEngland.csv', index=None)

        # Coloca en un bucket de S3 el texto parseado de cada uno de los sitios web en su
        # respectivo Path que se ve asi:
                # Key = 'headlines/raw/periodico=bbc/year=2022/month=04/day=30/rawBbc.txt'
        s3.upload_file('/tmp/dfBbc.csv', Bucket=nombreBucket, Key=directorioFinal+"bbc/"+path+"/dfBbc.csv")
        s3.upload_file('/tmp/dfEngland.csv', Bucket=nombreBucket, Key=directorioFinal+"journal/"+path+"/dfEngland.csv")

        return {}

def scrapBbc(page):
        soup = BeautifulSoup(page, 'html.parser')

        titular = soup.find_all('h3', class_='media__title')
        titulares = scrapText(titular)

        categoria = soup.find_all('a', class_='media__tag')
        categorias = scrapText(categoria)

        link = soup.find_all('a', class_='media__link', href=True)
        links = scrapLinks(link)

        dfBbc = pd.DataFrame({"titular":titulares, "categoria":categorias, "url":links}, index=[*range(0, len(titulares))])
        return dfBbc

def scrapJournal(page):
        soup = BeautifulSoup(page, 'html.parser')

        titular = soup.find_all('b', class_='m-article__title')
        titulares = scrapText(titular)

        categoria = soup.find_all('a', class_='m-article__type')
        categorias = scrapText(categoria)

        link = soup.find_all('a', class_='m-article__link', href=True)
        links = scrapLinks(link)

        dfEngland = pd.DataFrame({"titular":titulares, "categoria":categorias, "url":links}, index=[*range(0, len(titulares))])
        return dfEngland

def scrapText(listaScraping):
        items = list()
        for i in listaScraping:
                if i != "":
                        items.append(i.text.strip())
                else:
                        items.append(" ")
        return items

def scrapLinks(listaScraping):
        items = list()
        for i in listaScraping:
                items.append(i['href'])
        return items


