from datetime import datetime as dt


def log_type(name, data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"{time}  User name: {name}\nType of numbers: {data}\n")


def log_operation(data):
    time = dt.now().strftime('%D %H:%M')
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"Operation: {data}\n")


def log_data(data):
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"Numbers: {data}\n")


def log_result(data):
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(f"Result: {data}\n")
        f.write('-' * 100 + '\n')