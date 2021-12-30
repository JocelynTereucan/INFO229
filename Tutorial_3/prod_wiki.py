import pika
import sys
#import wikipedia

#Nuestra tarea pasada como argumento
message = ' '.join(sys.argv[1:]) or "wikipedia"

#Conexión al servidor RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

#Creación de la cola
channel.queue_declare(queue='hello')

#Publicación del mensaje
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=message)

print(" [x] search %r in wikipedia"%message)
connection.close()