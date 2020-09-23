from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Я постою')
        ],
        [
            KeyboardButton(text='Второй стул'),
            KeyboardButton(text='Первый стул')
        ],
    ],
    resize_keyboard=True
)