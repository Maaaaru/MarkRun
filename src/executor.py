import os

def executor(code_list):
    for cmd in code_list:
        res = os.system(cmd)