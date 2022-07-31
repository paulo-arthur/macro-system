from pynput import keyboard
from functools import partial
from json_tools import read_json, write_json, OS
from os import system
from subprocess import call



macros = read_json()

def on_activate(key):
    for macro in macros:
        if macro['key'] == key:
            try:
                if OS() == 'WINDOWS':
                    call(macro['exe_path'])
                elif OS() == 'UNIX':
                    system('bash ' + macro['exe_path'])
            except:
                print("Macro System can't find the file")


hotkeys = {}

for macro in macros:
    hotkeys['<ctrl>+<alt>+' + macro['key']] = partial(on_activate, macro['key'])

listener = keyboard.GlobalHotKeys(hotkeys)
listener.start()

while True:
    pass
