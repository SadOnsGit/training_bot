from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup

from db import course, web, guide
from keyboards.mkp_cancel import mkp_cancel
import os

cb_changes = Router()


class SetCourse(StatesGroup):
    title = State()
    text = State()


class SetWebinar(StatesGroup):
    title = State()
    text = State()
    file = State()


class SetGuide(StatesGroup):
    title = State()
    text = State()
    file = State()


class SetAdmin(StatesGroup):
    setadmin = State()


class SetUser(StatesGroup):
    setuser = State()


class DeleteCourse(StatesGroup):
    title = State()


class DeleteWebinar(StatesGroup):
    title = State()


class DeleteGuide(StatesGroup):
    title = State()

# Уроки


# Удаление урока
@cb_changes.message(DeleteCourse.title)
async def delete_lesson(message: Message, state: FSMContext):
    await course.delete_lesson(message.text)
    await message.answer(
        '<b>Успешно удалено</b>',
        parse_mode='html'
    )
    await state.clear()


# Создание урока
@cb_changes.callback_query(F.data.startswith('course.'))
async def course_changes(call: CallbackQuery, state: FSMContext):
    if call.data == 'course.add':
        await call.message.edit_text(
            '<b>Добавление урока. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(SetCourse.title)
    elif call.data == 'course.delete':
        await call.message.edit_text(
            '<b>Удаление урока. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(DeleteCourse.title)


@cb_changes.message(SetCourse.title)
async def setcoursetitle(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer(
        f'<b>Название урока: {title}. Введите текст урока: </b>',
        parse_mode='html',
        reply_markup=mkp_cancel)
    await state.set_state(SetCourse.text)


@cb_changes.message(SetCourse.text)
async def setcoursetext(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    lesson_data = await state.get_data()
    await course.add_lesson(lesson_data.get('title'), lesson_data.get('text'))
    await message.answer('<b>✅ Урок был успешно добавлен.</b>', parse_mode='html')
    await state.clear()


# Вебинары

# Удаление вебинара
@cb_changes.message(DeleteWebinar.title)
async def delete_webinar(message: Message, state: FSMContext):
    await web.delete_webinar(message.text)
    await message.answer(
        '<b>Успешно удалено</b>',
        parse_mode='html'
    )
    await state.clear()


# Создание вебинара
@cb_changes.callback_query(F.data.startswith('web.'))
async def web_changes(call: CallbackQuery, state: FSMContext):
    if call.data == 'web.add':
        await call.message.edit_text(
            '<b>Добавление вебинара. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(SetWebinar.title)
    elif call.data == 'web.delete':
        await call.message.edit_text(
            '<b>Удаление вебинара. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(DeleteWebinar.title)


@cb_changes.message(SetWebinar.title)
async def setwebtitle(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer(
        f'<b>Название вебинара: {title}. Введите текст вебинара: </b>',
        parse_mode='html',
        reply_markup=mkp_cancel
    )
    await state.set_state(SetWebinar.text)


@cb_changes.message(SetWebinar.text)
async def setwebtext(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(
        '<b>Отправьте файл, который будет прикреплён к вебинару.'
        '\nВ случае если файл не предусмотрен, напишите любой текст</b>',
        parse_mode='html'
    )
    await state.set_state(SetWebinar.file)


@cb_changes.message(SetWebinar.file)
async def setwebfile(message: Message, state: FSMContext):
    directory = 'webinars'
    if not os.path.exists(directory):
        os.makedirs(directory)
    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        file_path = await message.bot.get_file(file_id)
        await message.bot.download_file(file_path.file_path, f'{directory}/{file_name}')
        await state.update_data(file_path=f'{directory}/{file_name}')
        web_data = await state.get_data()
        await web.add_webinar(web_data.get('title'), web_data.get('text'), web_data.get('file_path'))
    else:
        web_data = await state.get_data()
        await web.add_webinar(web_data.get('title'), web_data.get('text'), None)
    await message.answer('<b>✅ Вебинар был успешно добавлен.</b>', parse_mode='html')
    await state.clear()


# Гайды

# Удаление гайда
@cb_changes.message(DeleteGuide.title)
async def delete_guide(message: Message, state: FSMContext):
    await guide.delete_guide(message.text)
    await message.answer(
        '<b>Успешно удалено</b>',
        parse_mode='html'
    )
    await state.clear()


# Создание гайда
@cb_changes.callback_query(F.data.startswith('guide.'))
async def guide_changes(call: CallbackQuery, state: FSMContext):
    if call.data == 'guide.add':
        await call.message.edit_text(
            '<b>Добавление гайда. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(SetGuide.title)
    elif call.data == 'guide.delete':
        await call.message.edit_text(
            '<b>Удаление гайда. Введите название: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(DeleteGuide.title)


@cb_changes.message(SetGuide.title)
async def setguidetitle(message: Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer(
        f'<b>Название гайда: {title}. Введите текст гайда: </b>',
        parse_mode='html',
        reply_markup=mkp_cancel
    )
    await state.set_state(SetGuide.text)


@cb_changes.message(SetGuide.text)
async def setguidetext(message: Message, state: FSMContext):
    text = message.text
    await state.update_data(text=text)
    await message.answer(
        '<b>Отправьте файл, который будет прикреплён к гайду.'
        '\nВ случае если файл не предусмотрен, напишите любой текст</b>',
        parse_mode='html'
    )
    await state.set_state(SetGuide.file)

@cb_changes.message(SetGuide.file)
async def setguidefile(message: Message, state: FSMContext):
    directory = 'guides'
    if not os.path.exists(directory):
        os.makedirs(directory)
    if message.document:
        file_id = message.document.file_id
        file_name = message.document.file_name
        file_path = await message.bot.get_file(file_id)
        await message.bot.download_file(file_path.file_path, f'{directory}/{file_name}')
        await state.update_data(file_path=f'{directory}/{file_name}')
        guide_data = await state.get_data()
        await guide.add_guide(guide_data.get('title'), guide_data.get('text'), guide_data.get('file_path'))
        await message.answer('<b>✅ Гайд был успешно добавлен.</b>', parse_mode='html')
    else:
        guide_data = await state.get_data()
        await guide.add_guide(guide_data.get('title'), guide_data.get('text'), None)
        await message.answer('<b>✅ Гайд был успешно добавлен.</b>', parse_mode='html')
    await state.clear()