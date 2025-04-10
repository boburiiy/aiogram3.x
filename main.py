from dispatcher.config import ADMINS, \
    bot, \
    dp, \
    setup_logging, \
    setup_commands, \
    notify_admins, \
    setup_handlers, \
    setup_callback_handlers, \
    bot_commands
from dispatcher.routing import routes, callback_routes
import asyncio


async def main():
    setup_logging()
    setup_callback_handlers(dp, callback_routes)
    setup_handlers(dp, routes)
    await setup_commands(bot, bot_commands)
    await notify_admins(bot, ADMINS)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
