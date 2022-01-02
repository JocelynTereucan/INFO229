import mysql.connector
import os, time
import pika
from urllib import parse, request
import re

HOST = os.environ['RABBITMQ_HOST']
print("rabbit:"+HOST)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channel = connection.channel()

#El consumidor utiliza el exchange 'cartero'
channel.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)

#Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
result = channel.queue_declare(queue="music", exclusive=True, durable=True)
queue_name = result.method.queue

#La cola se asigna a un 'exchange'
channel.queue_bind(exchange='cartero', queue=queue_name, routing_key="music")

def callback(ch, method, properties, body):
	print(body.decode("UTF-8"))
	arguments = body.decode("UTF-8").split(" ")

	if (arguments[0]=="!seach_music"):
		keywords = parse.urlencode({'search_query': arguments})
		html_result = request.urlopen('http://www.youtube.com/results?' + keywords)
		array_links=re.findall('href=\"\\/watch\\?v=(.{11})',html_result.read().decode('utf-8'))
		result = 'https://www.youtube.com/watch?v=' + array_links[0]
		channel.basic_publish(exchange='cartero',routing_key="discord_writer",body=result)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()