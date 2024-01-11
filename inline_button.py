from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup


top_music = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1', callback_data='janze'),
            InlineKeyboardButton(text='2', callback_data='maktab'),
            InlineKeyboardButton(text='3', callback_data='konsta'),
            InlineKeyboardButton(text='4', callback_data='yetmadi'),
            InlineKeyboardButton(text='5', callback_data='qizil'),
        ],
        [
            InlineKeyboardButton(text='➡', callback_data='right')
        ]
    ],
)

like_dislike = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='❤', callback_data='like'),
            InlineKeyboardButton(text='❌', callback_data='dislike')
        ]
    ]
)