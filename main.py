import asyncio
from config import dp, bot,notify_admins,set_commands
from hanlders import start, echo

async def main():
    await notify_admins('bot started',bot)
    await set_commands(bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        import logger
        asyncio.run(main())
    except KeyboardInterrupt:
        print('goodbye :-) 👋🏿')