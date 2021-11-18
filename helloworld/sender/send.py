import pika
import time

time.sleep(10)

credentials = pika.PlainCredentials('admin', 'admin')

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
                            'rabbitmq',
                            5672,
                            '/',
                            credentials))
channel = connection.channel()

channel.queue_declare(queue='hey')

for i in range(10):
    channel.basic_publish(exchange='', routing_key='hey', body=f'times: {i}')


print(" [x] Messages have been sent")
connection.close()
