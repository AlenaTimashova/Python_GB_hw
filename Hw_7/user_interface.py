
def choose_mode():
    mode = input('''Выберите действие:
            1. Импортировать данные
            2. Экспортировать данные
            3. Показать телефонный справочник
            4. Добавить данные в справочник
            Введите номер необходимого действия: ''')
    return mode

def get_data():
    data = []
    data.append(input('Введите фамилию: '))
    data.append(input('Введите имя: '))
    data.append(input('Введите номер телефона: '))
    data.append(input('Введите примечание: '))
    return data