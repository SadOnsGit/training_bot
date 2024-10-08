from aiogram.types import CallbackQuery
from aiogram import Router, F

from db import course, web, guide

cb_main = Router()

@cb_main.callback_query(F.data.startswith('getlesson.'))
async def getcourse(callback_query: CallbackQuery):
    lesson_id = callback_query.data.split('.')[1]
    text = await course.get_lesson_by_id(lesson_id)
    await callback_query.message.answer(text)


@cb_main.callback_query(F.data.startswith('getweb.'))
async def getweb(callback_query: CallbackQuery):
    web_id = callback_query.data.split('.')[1]
    text = await web.get_webinar_by_id(web_id)
    await callback_query.message.answer(text)


@cb_main.callback_query(F.data.startswith('getguide.'))
async def getguide(callback_query: CallbackQuery):
    guide_id = callback_query.data.split('.')[1]
    text = await guide.get_guide_by_id(guide_id)
    await callback_query.message.answer(text)
