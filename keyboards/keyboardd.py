from libs.libslist import *
from database.basesqlite3 import *

def add_newss():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = ['Предложить новость']
    keyboard.add(*buttons)
    return keyboard