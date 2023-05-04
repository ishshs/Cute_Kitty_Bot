from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(text="кошечка"))
    keyboard.add(KeyboardButton(text="собачка"))
    return keyboard