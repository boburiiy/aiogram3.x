from .config import ADMINS, Bot


async def notify_admins(message: str, bot: Bot, ADMINS: list = ADMINS):
    for admin in ADMINS:
        if admin:
            await bot.send_message(admin, message)
