from definitions import Task, MainProcess, SearchBaiduBaikeProcess, load_json_file
import pika
import json

def execute_step_logic(step_id, business_name, question):
    # 示例模拟逻辑
    if step_id == 'process_0002':
        # 根据业务名和问题模拟一些逻辑
        return f"模拟处理了业务: {business_name}, 问题: {question}"

def execute_baidu_baike_step_logic(step_id, business_name):
    if step_id == 'action_0001':
        # 根据业务名模拟查询百度百科
        return f"模拟在百度百科搜索: {business_name}"

def process_message(task, main_process, search_baidu_baike_process, message):
    business_name = message["inputs"]["business_name"]
    question = message["inputs"]["question"]

    print(f"处理任务: 业务 - {business_name}, 问题 - {question}")
    # 根据主处理流程和百度百科流程执行步骤
    for step in main_process.execution['steps']:
        result = execute_step_logic(step['id'], business_name, question)
        print(f"步骤结果: {result}")

    for step in search_baidu_baike_process.execution['steps']:
        result = execute_baidu_baike_step_logic(step['id'], business_name)
        print(f"百度百科步骤结果: {result}")

def on_message_received(ch, method, properties, body):
    message = json.loads(body)
    print(f"收到消息: {message}")

    task = Task(load_json_file('path/to/noun_exp.task.json'))
    main_process = MainProcess(load_json_file('path/to/main.process.json'))
    search_baidu_baike_process = SearchBaiduBaikeProcess(load_json_file('path/to/searchBaiduBaike.process.json'))

    process_message(task, main_process, search_baidu_baike_process, message)

def main():
    # connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    # channel = connection.channel()

    # channel.queue_declare(queue='task_queue')
    # channel.basic_consume(queue='task_queue', on_message_callback=on_message_received, auto_ack=True)

    # print('等待消息。退出请按 CTRL+C')
    # channel.start_consuming()
    
    # RabbitMQ服务器连接参数
    credentials = pika.PlainCredentials('test', 'Xu4Fg0Ut6Sf1')
    connection_params = pika.ConnectionParameters(
        host='121.37.27.62',
        port=15672,
        virtual_host='/',
        credentials=credentials
    )

    # 创建RabbitMQ连接
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # 声明队列，确保队列存在
    channel.queue_declare(queue='task_queue')

    # 设置回调函数处理接收到的消息
    channel.basic_consume(queue='task_queue', on_message_callback=on_message_received, auto_ack=True)

    print('等待消息。退出请按 CTRL+C')
    channel.start_consuming()

if __name__ == "__main__":
    main()
