"""
producer:
https://www.rabbitmq.com/tutorials/tutorial-one-python.html
"""
import time

import pika

# credentials = pika.PlainCredentials('', 'password')
# 建立连接

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', ))  # 创建连接对象
channel = connection.channel()  # 创建信道
channel.queue_declare(queue='hello3', durable=True)  # 声明队列
while True:
    channel.basic_publish(exchange='',
                          routing_key='hello3',
                          properties=pika.BasicProperties(
                              delivery_mode=2,  # make message persistent
                              content_type='application/json',
                              content_encoding='utf-8',
                          ),
                          body="hello, 世界!")
    time.sleep(1)
    print("[x] sent 'Hello 世界!'")
