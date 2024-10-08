from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mkp_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📈 Управление уроками',
                             callback_data='admin.setcourse')
    ],
    [
        InlineKeyboardButton(text='🎥 Управление вебинарами',
                             callback_data='admin.setweb')
    ],
    [
        InlineKeyboardButton(text='📚 Управление гайдами',
                             callback_data='admin.setguide')
    ],
    [
        InlineKeyboardButton(text='👥 Назначить администратора',
                             callback_data='admin.setadmin')
    ],
    [
        InlineKeyboardButton(text='➕ Добавить пользователя',
                             callback_data='admin.setuser')
    ]
])


course_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📚 Добавить урок',
                             callback_data='course.add')
    ],
    [
        InlineKeyboardButton(text='🗑️ Удалить урок',
                             callback_data='course.delete')
    ],
])


webinar_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📚 Добавить вебинар',
                             callback_data='web.add')
    ],
    [
        InlineKeyboardButton(text='🗑️ Удалить вебинар',
                             callback_data='web.delete')
    ],
])

guide_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='📚 Добавить гайд',
                             callback_data='guide.add')
    ],
    [
        InlineKeyboardButton(text='🗑️ Удалить гайд',
                             callback_data='guide.delete')
    ],
])