from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import KeyboardBuilder, ReplyKeyboardBuilder


def main_keyboard():
    keyboard_bilder = ReplyKeyboardBuilder()
    keyboard_bilder.button(text='Погода')
    keyboard_bilder.button(text='Котик')
    keyboard_bilder.button(text='Фото')

    keyboard_bilder.adjust(3)
    return keyboard_bilder.as_markup(resize_keyboard=True, input_field_placeholder='Что прислать ?')



