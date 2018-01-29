import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='durable_queue',durable=True)

message = " ".join(sys.argv[1:]) or "Hello world"
channel.basic_publish(exchange='',routing_key='durable_queue',
                      body=message,
                      properties=pika.BasicProperties(
                          delivery_mode=2,
                      ))

print(" [x] sent %r" % message)
connection.close()