from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Top50'),
            KeyboardButton('Milliy')
        ],
        [
            KeyboardButton('Jahon Estradasi'),
            KeyboardButton('Classic')
        ],
    ],
    resize_keyboard=True
)
