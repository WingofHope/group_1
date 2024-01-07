import json
from abc import ABC, abstractmethod

class Step(ABC):
    @abstractmethod
    def execute(self, data):
        pass

class Action(Step):
    def execute(self, data):
        print("执行 Action")
        # 在这里实现 action 的具体逻辑
        return "Action 结果"

class Generator(Step):
    def execute(self, data):
        print("执行 Generator")
        # 在这里实现 generator 的具体逻辑
        return "Generator 结果"

class Tool(Step):
    def execute(self, data):
        print("执行 Tool")
        # 在这里实现 tool 的具体逻辑
        return "Tool 结果"

def create_step(step_type):
    if step_type == 'action':
        return Action()
    elif step_type == 'generator':
        return Generator()
    elif step_type == 'tool':
        return Tool()
    else:
        raise ValueError("Unknown step type")
class Task:
    def __init__(self, task_json):
        self.id = task_json['id']
        self.name = task_json['name']
        self.description = task_json['description']
        self.inputs = task_json['inputs']
        self.process = task_json['process']

class MainProcess:
    def __init__(self, process_json):
        self.id = process_json['id']
        self.name = process_json['name']
        self.description = process_json['description']
        self.inputs = process_json['inputs']
        self.outputs = process_json['outputs']
        self.execution = process_json['execution']

class SearchBaiduBaikeProcess:
    def __init__(self, process_json):
        self.id = process_json['id']
        self.name = process_json['name']
        self.description = process_json['description']
        self.inputs = process_json['inputs']
        self.outputs = process_json['outputs']
        self.execution = process_json['execution']

def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)
