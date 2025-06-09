import json 

def get_json_file_data(file_path: str):
    file = open(file_path)
    data = json.load(file)
    return data
