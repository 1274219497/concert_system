import  pika

class RabbitMQSend():
    def __init__(self,body):
        # 1、连接rabbitmq服务器
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()

        # 2、创建一个名为hello的队列
        channel.queue_declare(queue='hello')
        # 3、简单模式,向名为hello队列中插入用户邮箱地址email
        channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=body,
                              )
        print("发送消息：‘{}’ 到MQ成功".format(body))
        connection.close()