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

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Hey~'
channel.basic_publish(
    exchange='topic_logs', routing_key=routing_key, body=message)
print(" [x] Sent %r:%r" % (routing_key, message))
connection.close()