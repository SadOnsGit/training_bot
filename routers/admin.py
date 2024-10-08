from aiogram import Router
from aiogram.filters import Command
from aiogram import types

from settings import config
from keyboards.mkp_admin import mkp_panel

admin_router = Router()

@admin_router.message(Command('admin'))
async def admin_panel(msg: types.Message):
    user_id = msg.from_user.id
    if user_id in config.get_admins():
        await msg.answer(f'<b>⚙️ Админ панель:</b>',
                        parse_mode='html', reply_markup=mkp_panel)
