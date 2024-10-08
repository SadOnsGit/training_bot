from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from db import guide, course, web


async def create_guide_keyboard():
    guides = await guide.get_guides()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    buttons = [
        [InlineKeyboardButton(text=guide_title, callback_data=f'getguide.{guide_id}')]
        for guide_id, guide_title in guides
    ]
    keyboard.inline_keyboard.extend(buttons)

    return keyboard


async def create_web_keyboard():
    webinars = await web.get_webinars()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    buttons = [
        [InlineKeyboardButton(text=web_title, callback_data=f'getweb.{web_id}')]
        for web_id, web_title in webinars
    ]
    keyboard.inline_keyboard.extend(buttons)
    return keyboard


async def create_lesson_keyboard():
    lessons = await course.get_lessons()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])
    buttons = [
        [InlineKeyboardButton(text=lesson_title, callback_data=f'getlesson.{lesson_id}')]
        for lesson_id, lesson_title in lessons
    ]
    keyboard.inline_keyboard.extend(buttons)

    return keyboard