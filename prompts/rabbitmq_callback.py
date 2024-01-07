import pika
import json

def callback(ch, method, properties, body):
    message = json.loads(body.decode('utf-8'))  # 解码消息内容
    print(f"Received message: {message}")

def consume_queue(queue_name='task_queue'):
    credentials = pika.PlainCredentials('test', 'Xu4Fg0Ut6Sf1')
    connection_params = pika.ConnectionParameters(
        host='121.37.27.62',
        port=5672,  # 使用 AMQP 端口
        virtual_host='/',
        credentials=credentials
    )

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print(f"Waiting for messages from queue {queue_name}. To exit press CTRL+C")
    channel.start_consuming()

if __name__ == "__main__":
    consume_queue()
