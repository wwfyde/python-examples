"""
comsumer:
"""

import pika
# credentials = pika.PlainCredentials('', 'password')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port='5672', ))  # 创建连接对象
channel = connection.channel()  # 创建信道
channel.queue_declare(queue='hello')  # 声明队列
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body="hello, 世界!")
print("[x] sent 'Hello 世界!'")
