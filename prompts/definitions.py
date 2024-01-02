import json

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
    with open(file_path, 'r') as file:
        return json.load(file)
