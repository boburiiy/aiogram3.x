from dispatcher.routing import routes, callback_routes, err_handler  # main event handlers
from config.config import *  # importing configuration
from router import routing  # importing router for include it
import asyncio


async def aynchronus_funcs():
    await asyncio.create_task(bot.delete_webhook(drop_pending_updates=True))  # deleting webhook for anycase
    await asyncio.sleep(.5)  # sleeping .5 seconds
    # setting up default commands
    await asyncio.create_task(setup_commands(bot, bot_commands))
    await asyncio.sleep(.5)
    await asyncio.create_task(notify_admins(bot, ADMINS))  # notifying admins
    await asyncio.sleep(.5)


def start_funcs():
    setup_logging()  # setting up logging
    setup_middlewares(dp, middlewares_list)  # setting up middlewares
    # setting up middlewares for callback handlers
    setup_callback__middlewares(dp, middlewares_list)

    setup_handlers(routers[0], routing.routes)  # including router handlers
    setup_handlers(dp, routes)  # including dp handlers
    setup_error_handlers(dp, err_handler)  # error handlers
    setup_callback_handlers(dp, callback_routes)  # including callback handlers

    setup_routers(dp, routers)  # including routers


async def main():
    
    await aynchronus_funcs()
    start_funcs()
    await dp.start_polling(bot) # starting polling

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped :)")
