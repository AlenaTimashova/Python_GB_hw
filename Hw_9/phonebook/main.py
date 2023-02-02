import user_interface as ui
import logger as lg
import crud


lg.logging.info('Start')
crud.init_data_base('base_phone.csv')
ui.ls_menu()