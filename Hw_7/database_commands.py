
def add_phonebook_items(data):
      
    with open ('phone_book.csv', 'a', encoding='utf-8') as file:
        for el in data:
            file.write(el + ' ')
        file.write('\n')
    print('Запись создана')

def show_phonebook():
    
    with open ('phone_book.csv', 'r', encoding='utf-8') as file:
        print(file.read())

def import_txt():
    with open (r'D:\GeekBrains\Python\Homeworks\Hw_7\my_import.txt', encoding='utf-8') as  mi:
        data_item = mi.readlines()
    
    with open ('phone_book.csv', 'a', encoding='utf-8') as file:
            for el in data_item:
                file.writelines(el)
    print('Данные импортированы. Телефонный справочник обновлен')  

def export_txt():
    with open ('phone_book.csv', 'r', encoding='utf-8') as file:
        data_item = file.readlines()
    
    with open ('export.txt', 'w', encoding='utf-8') as export_data:
        for el in data_item:
            export_data.writelines(el)
    print('Данные телефонного справочника экспортированы в файл')  