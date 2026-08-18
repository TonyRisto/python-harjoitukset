from datetime import datetime

current_time = datetime.now()
name = input("What is your name? ")


def greeting():
     return f'Hello, {name}!\nCurrent time: {current_time}'

welcome = greeting()

print(welcome)