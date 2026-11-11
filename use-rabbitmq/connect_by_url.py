import pika

# url = 'amqp://MjphbXFwLWNuLTV5ZDNmdWlldzAwNTpMVEFJNXRKZXRydHlBRHYxWjRKcjVMNEE=:RUI1M0ZDMjhCMjdGQjExRTQ2M0QxQzY0QTlFOTJGQTczNDM1NDcxMzoxNjk3NTIzOTMwMzI0@amqp-cn-5yd3fuiew005.cn-hangzhou.amqp-4.net.mq.amqp.aliyuncs.com:5672/molook-uat'
url = 'amqp://MjphbXFwLWNuLTV5ZDNmdWlldzAwNTpMVEFJNXRSMTlKNG5qVGJMTkFRWjIxMWs=:REUwRDM4ODQxNzAzMzg3NkY2QUZEQkZDRDFCMjEyRTkzMkI1MkZCMToxNzA3MTI2NDc1MDUx@amqp-cn-5yd3fuiew005.cn-hangzhou.amqp-4.net.mq.amqp.aliyuncs.com:5672/lanyun-test'

params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='hello8')

channel.basic_publish(exchange='',
                      routing_key='hello8',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          content_type='application/json',
                          content_encoding='utf-8',
                      ),
                      body="hello, 世界!")
channel.close()
connection.close()
