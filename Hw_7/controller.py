import user_interface as ui
import database_commands as dbc

def start_book():
    s = ui.choose_mode()
    if s == '1':
        dbc.import_txt()
    elif s == '2':
        dbc.export_txt()
    elif s == '3':
        dbc.show_phonebook()
    elif s == '4':
        data_item = ui.get_data()
        dbc.add_phonebook_items(data_item)
    else:
        print('Вы ввели неправильные данные. Попробуйте еще раз')
        ui.choose_mode()
  
