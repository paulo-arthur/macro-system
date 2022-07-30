import json, os

def OS():
     return 'WINDOWS' if os.name == 'nt' else 'UNIX'

def PATH():
    return os.path.abspath('.') + '/'

def read_json():
    json_macros = open('macros.json', 'r')
    macros = json.load(json_macros)
    return macros

def write_json(data):
    with open('macros.json', 'w') as macros:
        json.dump(data, macros, indent = 4)
        macros.close()
