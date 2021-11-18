import pika
import sys
import time

credentials = pika.PlainCredentials('admin', 'admin')

time.sleep(10)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(
                            'rabbitmq',
                            5672,
                            '/',
                            credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,
    ))
print(" [x] Sent %r" % message)
connection.close()
