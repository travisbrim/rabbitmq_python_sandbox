#!/usr/bin/env python
import pika
import sys

message = ' '.join(sys.argv[1:]) or 'Hello World!'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue2', durable=True)

channel.basic_publish(exchange='',
                      routing_key='task_queue2',
                      body=message,
                      properties=pika.BasicProperties(
                            delivery_mode=2
                      ))
print(" [x] Sent '{}'".format(message))

connection.close()
