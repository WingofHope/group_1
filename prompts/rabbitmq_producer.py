import pika
import json

def send_message_to_queue(message, queue_name='task_queue'):
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

    # 确保消息文本以UTF-8编码
    encoded_message = json.dumps(message, ensure_ascii=False).encode('utf-8')

    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=encoded_message)
    print(f"消息已发送到队列 {queue_name}")

    connection.close()

def main():
    task_message = {
        "id": "task_001",
        "inputs": {
            "business_name": "汽车制造",
            "question": "ECU是什么"
        }
    }

    send_message_to_queue(task_message)

if __name__ == "__main__":
    main()
# import pika
# import json

# def send_message_to_queue(message, queue_name='task_queue'):
#     credentials = pika.PlainCredentials('test', 'Xu4Fg0Ut6Sf1')
#     connection_params = pika.ConnectionParameters(
#         host='121.37.27.62',
#         port=5672,  # 注意更改为正确的端口
#         virtual_host='/',
#         credentials=credentials
#     )

#     connection = pika.BlockingConnection(connection_params)
#     channel = connection.channel()

#     channel.queue_declare(queue=queue_name)

#     channel.basic_publish(exchange='',
#                           routing_key=queue_name,
#                           body=json.dumps(message))
#     print(f"消息已发送到队列 {queue_name}")

#     connection.close()

# def main():
#     task_message = {
#         "id": "task_001",
#         "inputs": {
#             "business_name": "汽车制造",
#             "question": "ECU是什么？"
#         }
#     }

#     send_message_to_queue(task_message)

# if __name__ == "__main__":
#     main()