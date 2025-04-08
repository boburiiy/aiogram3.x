import sys
import asyncio
import logging
from handlers import dp
from config import bot, notify_admins, ADMINS


async def main():
    await notify_admins(bot, ADMINS)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('thanks for watching please subscribe 🔚')
else:print(__name__)