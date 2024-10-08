from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup

from keyboards.mkp_admin import course_panel, webinar_panel, guide_panel
from keyboards.mkp_cancel import mkp_cancel
from settings import config
from db import user


class SetAdmin(StatesGroup):
    setadmin = State()


class SetUser(StatesGroup):
    setuser = State()


cb_adminpanel = Router()


@cb_adminpanel.callback_query(F.data.startswith('admin.'))
async def admin_panel(call: CallbackQuery, state: FSMContext):
    if call.data == 'admin.setcourse':
        await call.message.edit_text(f'<b>📚 Управление уроками: </b>', parse_mode='html', reply_markup=course_panel)
    elif call.data == 'admin.setweb':
        await call.message.edit_text(f'<b>🎥 Управление вебинарами: </b>', parse_mode='html', reply_markup=webinar_panel)
    elif call.data == 'admin.setguide':
        await call.message.edit_text(f'<b>📖 Управление гайдами: </b>', parse_mode='html', reply_markup=guide_panel)
    elif call.data == 'admin.setadmin':
        await call.message.edit_text(
            '<b>✅ Введите айди нового администратора: </b>', 
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(SetAdmin.setadmin)
    elif call.data == 'admin.setuser':
        await call.message.edit_text(
            '<b>✅ Введите айди нового пользователя: </b>',
            parse_mode='html',
            reply_markup=mkp_cancel
        )
        await state.set_state(SetUser.setuser)


@cb_adminpanel.message(SetAdmin.setadmin)
async def setadmin(message: Message, state: FSMContext):
    try:
        admin = int(message.text)
    except ValueError:
        await message.reply("❌ Пожалуйста, введите корректное целое число (ID).")
        return
    config.set_admin(admin)
    await message.answer(f'<b>✅ Вы успешно добавили нового админа {admin}.</b>', parse_mode='html')
    await state.clear()


@cb_adminpanel.message(SetUser.setuser)
async def setuser(message: Message, state: FSMContext):
    try:
        userid = int(message.text)
    except ValueError:
        await message.reply("❌ Пожалуйста, введите корректное целое число (ID).")
        return
    await user.add_user(userid)
    await message.answer(f'<b>✅ Вы успешно добавили нового пользователя {userid}.</b>', parse_mode='html')
    await state.clear()
