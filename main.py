from config.config import (
    ADMINS,
    bot,
    dp,
    setup_logging,
    setup_commands,
    notify_admins,
    setup_handlers,
    setup_callback_handlers,
    bot_commands
)
from dispatcher.routing import routes, callback_routes
import asyncio


async def aynchronus_funcs():
    await asyncio.create_task(bot.delete_webhook(drop_pending_updates=True))
    await asyncio.sleep(.5)
    await asyncio.create_task(setup_commands(bot, bot_commands))
    await asyncio.sleep(.5)
    await asyncio.create_task(notify_admins(bot, ADMINS))
    await asyncio.sleep(.5)


def start_funcs():
    setup_logging()
    setup_callback_handlers(dp, callback_routes)
    setup_handlers(dp, routes)


async def main():
    await aynchronus_funcs()
    start_funcs()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
