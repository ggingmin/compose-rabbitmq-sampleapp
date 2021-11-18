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

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hey~'
channel.basic_publish(
    exchange='direct_logs', routing_key=severity, body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()