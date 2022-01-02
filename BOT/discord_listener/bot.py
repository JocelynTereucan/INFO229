import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import threading
import pika
import asyncio

HOST = os.environ('RABBITMQ_HOST')
print("rabbit:"+HOST)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=HOST))
channelMQ = connection.channel()

#Creamos el exchange 'cartero' de tipo 'fanout'
channelMQ.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!') #creando un bot

@bot.event #declarar eventos
async def on_ready(): #evento para cuando el bot se conecta
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    for channel in bot.get_all_channels():
        print(channel)
        print(channel.id)

    channel = bot.get_channel(913706828502814760)
    await channel.send('¡Hola!')


@bot.event
async def on_message(message): #se activa cuando hay un mensaje en el canal
    if message.author == bot.user: #verifica si no es él mismo quien envio el mensaje, para que no haya bucle
        return

    if message.content == 'pizza' or message.content == 'cerveza' or message.content == 'donuts': #si recibe pizza, donuts o cerveza, reacciona con lo que siguento 
        response = "!mmm..."+message.content+"!"
        await message.channel.send(response)

    await bot.process_commands(message)

@bot.command(name='birthday', help='Muestra la fecha de cumpleaño del miembro de la GUILD que se pasa en parámetro. Ejemplo: !birthday MatthieuVernier')
async def cumpleaños(ctx): #ctx es un contexto
    message =  ctx.message.content
    print("send a new mesage to rabbitmq: "+message)

    channelMQ.basic_publish(exchange='cartero', routing_key="birthday", body=message)

@bot.command(name='add-birthday', help='Permite añadir el cumpleaño de un nuevo miembro de la GUILD que se pasa en parámetro. Ejemplo: !add-birthday MatthieuVernier 1985-02-13')
async def cumpleaños(ctx):
    message =  ctx.message.content
    print("send a new mesage to rabbitmq: "+message)
    channelMQ.basic_publish(exchange='cartero', routing_key="birthday", body=message)

@bot.command(name='greeting-birthday', help='Muestra un saludo de cumpleaños a los miembros de la GUILD, que estan de cumpleaños en la fecha que se pasa en el parametro. Ejemplo !greeting-birthday 1985-02-13')
async def cumpleaños(ctx):
    message =  ctx.message.content
    print("send a new mesage to rabbitmq: "+message)
    channelMQ.basic_publish(exchange='cartero', routing_key="birthday", body=message)

@bot.command(name='seach_music', help='Muestra una recomendacion de YouTube, en relación al parametro ingresado. Ejemplo: !seach_music año nuevo')
async def music(ctx, str_ : str):
    message =  ctx.message.content                                                         
    print("send a new mesage to rabbitmq: "+message)                                       
    channelMQ.basic_publish(exchange='cartero', routing_key="music", body=message)       

def writer(bot):
    """thread worker function"""
    print('Worker')

    HOST = os.environ['RABBITMQ_HOST']

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=HOST))
    channelMQ = connection.channel()

    #Creamos el exchange 'cartero' de tipo 'fanout'
    channelMQ.exchange_declare(exchange='cartero', exchange_type='topic', durable=True)

    #Se crea un cola temporaria exclusiva para este consumidor (búzon de correos)
    result = channelMQ.queue_declare(queue="discord_writer", exclusive=True, durable=True)
    queue_name = result.method.queue

    #La cola se asigna a un 'exchange'
    channelMQ.queue_bind(exchange='cartero', queue=queue_name, routing_key="discord_writer")


    print(' [*] Waiting for messages. To exit press CTRL+C')

    async def write(message):
        channel = bot.get_channel(908505071887732768)#913706828502814760
        await channel.send(message)

    def callback(ch, method, properties, body):
        message=body.decode("UTF-8")
        print(message)

        bot.loop.create_task(write(message))

    channelMQ.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

    channelMQ.start_consuming()

t = threading.Thread(target=writer, args=[bot])
t.start()

bot.run(TOKEN)