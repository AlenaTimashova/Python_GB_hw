import logging

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

from bot import TOKEN
import calc
import log


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

TYPE, ACTION, NUMBERS, RESULT, MENU = range(5)

numbers_type = ''
action_type = ''


def start(update: Update, _):
    start_keyboard = [['Start']]
    markup = ReplyKeyboardMarkup(start_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(f'Hello {update.effective_user.first_name}! {chr(128075)}\n'
                              f'I am Calculator! {chr(128425)}{chr(129299)} I can work with rational and complex numbers.\n'
                              f'If you want to exit, enter /cancel.\n\n'
                              "Let's start?",
                              reply_markup=markup)
    return TYPE


def type_numbers(update: Update, _):
    type_keyboard = [['Rational', 'Complex']]
    markup = ReplyKeyboardMarkup(type_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Choose type of numbers you want to work with.', reply_markup=markup)
    return ACTION


def action(update: Update, _):
    global numbers_type
    user = update.message.from_user
    log.log_type(user.first_name, update.message.text)
    numbers_type = update.message.text
    action_keyboard = [['+', '-', '*', '/', '**']]
    markup = ReplyKeyboardMarkup(action_keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Choose action.', reply_markup=markup)
    return NUMBERS


def numbers(update: Update, _):
    global numbers_type, action_type
    log.log_operation(update.message.text)
    action_type = update.message.text
    if numbers_type == 'Rational':
        update.message.reply_text('Enter 2 numbers separated by space.')
    elif numbers_type == 'Complex':
        update.message.reply_text('Enter 4 numbers separated by space.')
    return RESULT


def result(update: Update, _):
    global numbers_type, action_type
    reply_keyboard = [['Continue'], ['Exit']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    nums = update.message.text
    n = nums.replace('.', '').replace(' ', '')
    numbers_list = nums.split()
    if n.isdigit() and (len(numbers_list) == 2 or len(numbers_list) == 4):
        if numbers_type == 'Rational' and len(numbers_list) == 2:
            if numbers_list[1] == '0' and action_type == '/':
                update.message.reply_text(f'Error! {chr(9940)} Division by 0!\n'
                                           'Try again.')
                return RESULT
            else:
                nums = nums.replace(' ', action_type)
                result = eval(nums)
                update.message.reply_text(f'Result {chr(128073)}: {nums}={result}\n'
                                        'What do you want to do next?', reply_markup=markup)
                log.log_data(update.message.text)
                log.log_result(result)
                return MENU
        elif numbers_type == 'Complex' and len(numbers_list) == 4:
            if numbers_list[2] == '0' or numbers_list[3] == '0' and action_type == '/':
                update.message.reply_text(f'Error! {chr(9940)} Division by 0!\n'
                                           'Try again.')
                return RESULT
            else:
                result = calc.compl(nums, action_type)
                update.message.reply_text(f'Result {chr(128073)}:' 
                                        f'{complex(int(numbers_list[0]), int(numbers_list[1]))}{action_type}{complex(int(numbers_list[2]), int(numbers_list[3]))}={result}\n'
                                        'What do you want to do next?', reply_markup=markup)
                log.log_data(update.message.text)
                log.log_result(result)
                return MENU
        else:
            if numbers_type == 'Rational':
                update.message.reply_text(f'Incorrect input! {chr(9940)}\n'
                                        'Enter 2 numbers separated by space.')
            elif numbers_type == 'Complex':
                update.message.reply_text(f'Incorrect input! {chr(9940)}\n'
                                        'Enter 4 numbers separated by space.')
            return RESULT
    else:
        if numbers_type == 'Rational':
            update.message.reply_text(f'Incorrect input! {chr(9940)}\n'
                                      'Enter 2 numbers separated by space.')
        elif numbers_type == 'Complex':
            update.message.reply_text(f'Incorrect input! {chr(9940)}\n'
                                      'Enter 4 numbers separated by space.')
        return RESULT


def menu(update: Update, _):
    global action_type
    action_type = update.message.text
    type_keyboard = [['Rational', 'Complex']]
    markup = ReplyKeyboardMarkup(type_keyboard, one_time_keyboard=True, resize_keyboard=True)
    if action_type == 'Continue':
        update.message.reply_text(f"OK! {chr(128077)}\n"
                                  'Choose type of numbers you want to work with.', reply_markup=markup)
        return ACTION
    elif action_type == 'Exit':
        update.message.reply_text(f'Bye! See you later! {chr(128521)}')
        return ConversationHandler.END


def exit(update: Update, _):
    update.message.reply_text(f'Bye! See you later! {chr(128521)}')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            TYPE: [MessageHandler(Filters.regex('^(Start)$'), type_numbers)],
            ACTION: [MessageHandler(Filters.text, action)],
            NUMBERS: [MessageHandler(Filters.text, numbers)],
            RESULT: [MessageHandler(Filters.text, result)],
            MENU: [MessageHandler(Filters.text, menu)]
        },

        fallbacks=[CommandHandler('cancel', exit)],
    )

    dispatcher.add_handler(conv_handler)

    updater.start_polling()
    updater.idle()