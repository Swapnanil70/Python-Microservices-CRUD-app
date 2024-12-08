import pika, json

params = pika.URLParameters('amqps://zgtmsdlf:WHK8zsNEGitN5tPMPxRneFFNCBixDqLc@gerbil.rmq.cloudamqp.com/zgtmsdlf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body.decode())
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

channel.close()