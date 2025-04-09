from dispatcher.config import ADMINS, bot, dp, setup_logging, setup_commands, notify_admins, setup_handlers, bot_commands
from dispatcher.routing import routes
import asyncio


async def main():
    setup_logging()
    await setup_commands(bot, bot_commands)
    await notify_admins(bot, ADMINS)
    setup_handlers(dp, routes)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped.")
