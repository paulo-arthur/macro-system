import os, json

OS = 'WINDOWS' if os.name == 'nt' else 'UNIX'
PATH = os.path.abspath('.') + '/'

def read_json():
    json_macros = open('macros.json', 'r')
    macros = json.load(json_macros)
    return macros

def write_json(data):
    with open('macros.json', 'w') as macros:
        json.dump(data, macros, indent = 4)
        macros.close()

def new_macro():
    key = input('CTRL + ALT + ')
    while not key.lower().isalpha() or len(key) != 1:
        print('Please type a letter')
        key = input('CTRL + ALT + ')

    file = input('name of executable: ')

    if OS == 'win':
        file = PATH + file + '.exe'
    else:
        file = PATH + file + '.deb'

    macro = {'key': key, 'exe_path': file}

    macros = read_json()
    macros.append(macro)
    write_json(macros)


try:
    macros = read_json()
except:
    write_json([])

print('Macro System - New Macro')
key = new_macro()
