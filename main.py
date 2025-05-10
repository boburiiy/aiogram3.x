from config.config import *
from dispatcher.routing import routes, callback_routes, err_handler
import router
import asyncio

import router.base_router
import router.handlers
import router.handlers.default
import router.routing


async def aynchronus_funcs():
    await asyncio.create_task(bot.delete_webhook(drop_pending_updates=True))
    await asyncio.sleep(.5)
    await asyncio.create_task(setup_commands(bot, bot_commands))
    await asyncio.sleep(.5)
    await asyncio.create_task(notify_admins(bot, ADMINS))
    await asyncio.sleep(.5)


def start_funcs():
    setup_logging()
    setup_middlewares(dp, middlewares_list)
    setup_error_handlers(dp, err_handler)
    setup_handlers(router.base_router.r1, router.routing.routes)
    # setup_routers(dp, routers)
    setup_handlers(dp, routes)
    setup_callback_handlers(dp, callback_routes)
    setup_callback__middlewares(dp, middlewares_list)


async def main():
    router.base_router.r1.message.register(router.handlers.default.echo)
    dp.include_router(router.base_router.r1)
    await aynchronus_funcs()
    start_funcs()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped :)")
