import asyncio
from config import dp, bot, routers, notify_admins, set_commands, setup_logging, setup_routers
from handlers import default_router

async def main():
    await notify_admins('bot started', bot)
    await set_commands(bot)
    setup_routers(routers, dp)
    default_router.message.middleware(CounterMiddleware())
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        setup_logging()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('goodbye :-) 👋🏿')
