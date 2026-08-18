from datetime import datetime

current_time = datetime.now()
name = "Tony Risto"


def greeting():
     return f'Hello, {name}!\nCurrent time: {current_time}'

welcome = greeting()

print(welcome)