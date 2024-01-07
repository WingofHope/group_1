from definitions import Task, MainProcess, SearchBaiduBaikeProcess, load_json_file, create_step
# 调用外部模块后启用
# from generator_engine import generator_engine  # 假设 generator_engine.py 中有一个名为 generator_engine 的函数
from tool_engine import tool_engine          # 假设 tool_engine.py 中有一个名为 tool_engine 的函数
# from action_engine import action_engine      # 假设 action_engine.py 中有一个名为 action_engine 的函数

import pika
import json
import subprocess

# def execute_step_logic(step_id, business_name, question):
#     # 示例模拟逻辑
#     if step_id == 'process_0002':
#         # 根据业务名和问题模拟一些逻辑
#         return f"模拟处理了业务: {business_name}, 问题: {question}"

# def execute_baidu_baike_step_logic(step_id, business_name):
#     if step_id == 'action_0001':
#         # 根据业务名模拟查询百度百科
#         return f"模拟在百度百科搜索: {business_name}"

def process_message(task, main_process, search_baidu_baike_process, message):
    business_name = message["inputs"]["business_name"]
    question = message["inputs"]["question"]

    print(f"处理任务: 业务 - {business_name}, 问题 - {question}")

    # 处理百度百科流程的步骤
    for step in search_baidu_baike_process.execution['steps']:
        step_id = step['id']
        if step_id == 'action_0001':
            # 处理 action_0001 步骤
            result = handle_action_0001(business_name)
        elif step_id == 'generator_0001':
            # 处理 generator_0001 步骤
            result = handle_generator_0001(business_name, question)
        elif step_id == 'tool_0002':
            # 处理 tool_0002 步骤
            result = handle_tool_0002(business_name)
        elif step_id == 'generator_0002':
            # 处理 generator_0002 步骤
            result = handle_generator_0002(business_name, question)
        print(f"步骤 {step_id} 结果: {result}")

# # 如果调用外部模块后启用
# def process_message(task, main_process, search_baidu_baike_process, message):
#     business_name = message["inputs"]["business_name"]
#     question = message["inputs"]["question"]

#     print(f"处理任务: 业务 - {business_name}, 问题 - {question}")

#     # 处理百度百科流程的步骤
#     for step in search_baidu_baike_process.execution['steps']:
#         step_id = step['id']
#         if step_id == 'action_0001':
#             result = action_engine(business_name)  # 调用 action_engine 函数
#         elif step_id == 'generator_0001':
#             result = generator_engine(business_name, question)  # 调用 generator_engine 函数
#         elif step_id == 'tool_0002':
#             result = tool_engine(business_name)  # 调用 tool_engine 函数
#         elif step_id == 'generator_0002':
#             result = generator_engine(business_name, question)  # 再次调用 generator_engine 函数
#         print(f"步骤 {step_id} 结果: {result}")


# 根据需要定义上述函数
def handle_action_0001(business_name):
    # 模拟过滤行业名词
    if business_name:
        return f"过滤后的行业名词: {business_name}"
    else:
        return "未提供有效的行业名词"
    
# 上面的是整体的模块替换，这里单独进行举例方便理解
# from generator_engine import some_function_in_generator

# def handle_generator_0001(business_name, question):
#     # 在这里，我们将 'business_name' 和 'question' 作为参数传递给 generator_engine 模块中的函数
#     result = some_function_in_generator(business_name, question)
#     return result

# 这一部分只是模拟，不是真实，接口已放在上面和下面，两种方式调用
def handle_generator_0001(business_name, question):
    # 模拟生成百度百科搜索关键字
    return f"搜索关键字: {business_name} 关于 {question}"

def handle_tool_0002(business_name):
    # 模拟获取百度百科简要信息
    return f"百度百科关于 '{business_name}' 的简要信息"

def handle_generator_0002(business_name, question):
    # 模拟根据百科描述回答用户的问题
    return f"根据百度百科关于 '{business_name}' 的信息，解答问题 '{question}'"

# 调用外部脚本，引入额外的性能开销和复杂性。看情况吧。这里使用的是脚本
# def call_external_script(script_name, data):
#     # 将数据转换为JSON字符串
#     input_str = json.dumps(data)

#     # 调用外部Python脚本并传递JSON字符串
#     result = subprocess.run(['python', script_name, input_str], capture_output=True, text=True)

#     # 解析返回的JSON字符串
#     if result.returncode == 0:
#         return json.loads(result.stdout)
#     else:
#         raise Exception(f"Script {script_name} failed: {result.stderr}")

# def handle_action_0001(business_name):
#     # 调用 action_engine.py 脚本
#     return call_external_script('action_engine.py', {'business_name': business_name})

# def handle_generator_0001(business_name, question):
#     # 调用 generator_engine.py 脚本
#     return call_external_script('generator_engine.py', {'business_name': business_name, 'question': question})

# def handle_tool_0002(business_name):
#     # 调用 tool_engine.py 脚本
#     return call_external_script('tool_engine.py', {'business_name': business_name})

# def handle_generator_0002(business_name, question):
#     # 再次调用 generator_engine.py 脚本
#     return call_external_script('generator_engine.py', {'business_name': business_name, 'question': question})

def on_message_received(ch, method, properties, body):
    message = json.loads(body.decode('utf-8'))
    print(f"收到消息: {message}")

    task = Task(load_json_file('prompts/task/noun_exp.task.json'))
    main_process = MainProcess(load_json_file('prompts/process/main.process.json'))
    search_baidu_baike_process = SearchBaiduBaikeProcess(load_json_file('prompts/process/searchBaiduBaike.process.json'))

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
        port=5672,  # 使用 AMQP 端口
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

    print('等待消息')
    channel.start_consuming()

if __name__ == "__main__":
    main()
