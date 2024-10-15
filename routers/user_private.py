from aiogram import Router
from aiogram.filters import Command
from aiogram import types

from keyboards.mkp_main import mkp_main
from keyboards.mkp_all import create_guide_keyboard, create_lesson_keyboard, create_web_keyboard

from db import user


router_start = Router()


@router_start.message(Command('start'))
async def start_message(msg: types.Message):
    user_id = msg.from_user.id
    if await user.user_access_exists(user_id):
        photo_url = 'https://i.imgur.com/8G38KWJ.jpeg'
        await msg.answer_photo(
            photo=photo_url,
            caption=(
                f'<b>Привет, {msg.from_user.full_name}!</b>\n\n'
                '<b>Добро пожаловать на курс <i>МЕДИАФОТОГРАФ</i> 💘</b>\n\n'
                'В этом боте ты получишь доступ ко всем материалам:\n\n'
                
                '✨ <b>УРОКИ:</b> Основные уроки с домашними заданиями, выполняя которые ты соберешь свое портфолио.\n\n'
                
                '🎥 <b>ВЕБИНАРЫ:</b> Вся подробная информация о работе фотографа / контент мейкера в медиа, которая поможет тебе стать настоящим профи.\n\n'
                
                '📚 <b>ГАЙДЫ:</b> Дополнительные материалы.\n\n'
                
                '📊 Прикрепляю таблицу, в каком порядке лучше смотреть уроки, чтобы максимально усвоить, отработать полученную информацию и не запутаться!\n\n'
                
                '<b>Хорошего обучения!</b>\n'
                'xo xo, foxikris 💋'
            ),
            parse_mode='html',
            reply_markup=mkp_main
        )
    else:
        await msg.answer(
            f'Для получения доступа к боту, отправь свой ID в личные сообщения @foxikrisss\n\nВаш ID: `{user_id}`',
            parse_mode='MARKDOWN'
        )


@router_start.message(lambda message: message.text == '📚 УРОКИ')
async def handle_lessons(message: types.Message):
    user_id = message.from_user.id
    if await user.user_access_exists(user_id):
        keyboard = await create_lesson_keyboard()
        await message.answer(
            "<b>Список доступных вам уроков.</b>",
            parse_mode='html',
            reply_markup=keyboard
        )


@router_start.message(lambda message: message.text == '💻 ВЕБИНАРЫ')
async def handle_webinars(message: types.Message):
    user_id = message.from_user.id
    if await user.user_access_exists(user_id):
        keyboard = await create_web_keyboard()
        await message.answer(
            "<b>Список доступных вам вебинаров.</b>",
            parse_mode='html',
            reply_markup=keyboard
        )


@router_start.message(lambda message: message.text == '📝 ГАЙДЫ')
async def handle_guides(message: types.Message):
    user_id = message.from_user.id
    if await user.user_access_exists(user_id):
        keyboard = await create_guide_keyboard()
        await message.answer(
            "<b>Список доступных вам гайдов.</b>",
            parse_mode='html',
            reply_markup=keyboard
        )
