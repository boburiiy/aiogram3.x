import logging
import sys
logging.basicConfig(
    level=logging.INFO,
    format='#%(levelname)s %(asctime)s %(process)d %(filename)s:%(lineno)d %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    stream=sys.stdout
)
