import json

def get_question_json():
    with open('config.json', 'r', encoding='utf-8') as file:
        Badjson = file.read()
        file.close()
    return json.loads(Badjson)