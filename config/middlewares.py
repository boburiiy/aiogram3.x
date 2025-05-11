from middlewares.base_middleware import Throttling
# icluding middlewares
middlewares_list = [
    Throttling(.25)
]
