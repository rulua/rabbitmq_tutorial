import pika
import sys
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',exchange_type='fanout')
curt = time.time()
message = ' '.join(sys.argv[:1],) or "information:hello world"

channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)

print(" [x] sent %r" %message)
connection.close()