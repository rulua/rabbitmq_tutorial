import pika

connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
'''
We're connected now, to a broker on the local machine - hence the localhost.
If we wanted to connect to a broker on a different machine we'd simply specify its name or IP address here.
'''
channel = connection.channel()
channel.queue_declare(queue="hello")
'''
Next, before sending we need to make sure the recipient queue exists. If we send a message to non-existing location,
RabbitMQ will just drop the message. Let's create a hello queue to which the message will be delivered:
 Our first message will just contain a string Hello World! and we want to send it to our hello queue.
 In RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
'''
channel.basic_publish(exchange='',routing_key='hello',body='{topic:I hate the world,'
                                                           'author:luru}')
'''
This exchange is special ‒ it allows us to specify exactly to which queue the message should go. 
The queue name needs to be specified in the routing_key parameter:
'''

print("[x] send 'hello luru'")
connection.close()