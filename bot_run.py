import asyncio


from bot_create import dp, bot
from routers.user_private import router_start
from routers.admin import admin_router
from callbacks import cb_adminpanel, cb_changes, cb_main, cb_cancel
from db import user

dp.include_routers(
    cb_changes.cb_changes,
    cb_adminpanel.cb_adminpanel,
    cb_main.cb_main,
    cb_cancel.cb_cancel_router,
    router_start,
    admin_router,
)


async def main():
    """Главная функция старта бота"""
    await user.create_tables()
    await dp.start_polling(bot)

asyncio.run(main())
