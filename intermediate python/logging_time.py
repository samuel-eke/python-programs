import logging
import time
from logging.handlers import TimedRotatingFileHandler

#keeps running based on the time the application is running
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=100, backupCount=5)
logger.addHandler(handler)

for _ in range(100):
    logger.info('hwouw')
    time.sleep(23)