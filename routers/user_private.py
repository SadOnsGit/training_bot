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
        await msg.answer(
            f'<b>Главное меню, {msg.from_user.full_name}!</b>',
            parse_mode='html',
            reply_markup=mkp_main
        )
    else:
        await msg.answer(
            f'<b>У вас нет доступа к боту. Ваш ID: {msg.from_user.id}</b>',
            parse_mode='html'
        )


@router_start.message(lambda message: message.text == '📚 УРОКИ')
async def handle_lessons(message: types.Message):
    keyboard = await create_lesson_keyboard()
    await message.answer(
        "<b>Список доступных вам уроков.</b>",
        parse_mode='html',
        reply_markup=keyboard
    )


@router_start.message(lambda message: message.text == '💻 ВЕБИНАРЫ')
async def handle_webinars(message: types.Message):
    keyboard = await create_web_keyboard()
    await message.answer(
        "<b>Список доступных вам вебинаров.</b>",
        parse_mode='html',
        reply_markup=keyboard
    )


@router_start.message(lambda message: message.text == '📝 ГАЙДЫ')
async def handle_guides(message: types.Message):
    keyboard = await create_guide_keyboard()
    await message.answer(
        "<b>Список доступных вам гайдов.</b>",
        parse_mode='html',
        reply_markup=keyboard
    )
