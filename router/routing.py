from config.setups import rout
from .handlers.default import echo
routes = [
    rout(echo)
]
