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

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hey!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent %r" % message)
connection.close()