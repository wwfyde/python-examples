"""
consumer:

"""
import os
import sys

import pika


def main():
    url = 'amqp://guest:guest@localhost:5672/'
    connection = pika.BlockingConnection(pika.URLParameters(url))  # 创建连接对象
    channel = connection.channel()  # 创建信道
    channel.queue_declare(queue='hello', durable=True)  # 声明队列

    # connection.close()
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")

    channel.basic_consume(queue='hello',
                          auto_ack=True,
                          on_message_callback=callback)

    # 创建事件循环
    channel.start_consuming()


if __name__ == '__main__':
    try:
        print("start consuming...")
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
