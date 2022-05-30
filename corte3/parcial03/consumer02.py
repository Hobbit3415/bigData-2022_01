from kafka import KafkaConsumer
import statistics
import boto3

consumer = KafkaConsumer("quickstart-events", bootstrap_servers=['localhost:9092'])
s3 = boto3.client('s3')

suma = 0
cont = 0
precios = list()

nombreBucket = 'parcial03'
directory_name = 'precios/'

for message in consumer:
    cont = cont+1
    precio = int(message[6].decode("utf-8"))
    precios.append(precio)
    suma = suma + precio
    promedio = suma/cont

    txt_data="{}. Promedio = {}".format(cont, str(promedio))
    print("Precio promedio: {}".format(str(promedio)))
    print("Archivo escrito")
    s3.put_object(Body=txt_data, Bucket='parcial03', Key=(directory_name+'precios.txt'))
