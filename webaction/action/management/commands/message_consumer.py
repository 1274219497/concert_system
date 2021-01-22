import pika
from action import actionPonse as ap
# ########################## 消费者 ##########################
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    newbody=str(body)[2:-1]
    print(newbody)
    tmpstr=list(str(newbody).split(" "))
    count=int(tmpstr[0])
    stu_num=[]
    for i in range(1,1+count):
        stu_num.append(str(tmpstr[i]))
    tkid=str(tmpstr[-2])
    concertid=str(tmpstr[-1])
    print("购票数量:"+str(count))
    print("购票人证件号列表:")
    print(stu_num)
    print("门票id:"+str(tkid))
    print("演唱会id:"+str(concertid))
    print(ap.actionResponse(count,stu_num,tkid,concertid))

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()