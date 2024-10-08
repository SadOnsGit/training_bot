from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


mkp_main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📚 УРОКИ')],
        [KeyboardButton(text='💻 ВЕБИНАРЫ')],
        [KeyboardButton(text='📝 ГАЙДЫ')]
    ],
    resize_keyboard=True
)
