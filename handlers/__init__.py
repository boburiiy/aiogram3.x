from handlers.routrs import default_router
from handlers.default_handlers import echo, start

routers = [default_router]

__all__ = ['default_router']
