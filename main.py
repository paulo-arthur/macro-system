import os, json
from json_tools import read_json, write_json, OS, PATH

if OS() == 'WINDOWS':
    import getpass
    try:
        STARTUP_DIR = f'C:/Users/{getpass.getuser()}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup'
        STARTUP_EXE = open(STARTUP_DIR + r'\macro-system-startup.bat', 'w')
        STARTUP_EXE.write('python ' + PATH() + '\main.py')
    except:
        print('Could not create initial run file')

def new_macro():
    key = input('CTRL + ALT + ')

    USED_KEYS = []
    for macro in read_json():
        USED_KEYS.append(macro['key'])

    if not key.lower().isalpha() or len(key) != 1:
        print('Please type a letter')
        new_macro()
    elif key.lower() in USED_KEYS:
        print('This key is already attached')
        new_macro()

    file = input('name of executable: ')

    if OS() == 'WINDOWS':
        file = PATH() + 'executables/' + file + '.bat'
    else:
        file = PATH() + 'executables/' + file + '.sh'

    macro = {'key': key, 'exe_path': file}

    macros = read_json()
    macros.append(macro)
    write_json(macros)


try:
    macros = read_json()
except:
    write_json([])

print('Macro System - New Macro')
print('Some hotkeys can conflict with operatinal system shortcuts.')
key = new_macro()
