from kafka import KafkaConsumer
import statistics
import boto3
consumer = KafkaConsumer("quickstart-events", bootstrap_servers=['localhost:9092'])
s3 = boto3.client('s3')

maximo = 1408000
minimo = 1407500

for message in consumer:
    precio = int(message[6].decode("utf-8"))

    if precio > maximo:
        print("************************************************")
        print("El precio está por encima del máximo establecido\nPrecio: {}\tMáximo: {}".format(precio, maximo))
        print("************************************************")

    elif precio < minimo:
        print("************************************************")
        print("El precio está por debajo del mínimo establecido\nPrecio: {}\tMínimo: {}".format(precio, minimo))
        print("************************************************")
