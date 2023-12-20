import logging

logger = logging.getLogger(__name__)

#create handler
stream_h = logging.StreamHandler() 
file_h = logging.FileHandler('file.log') #loggs to a file

#set level and format for each logger above
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

#setting the format for the logger
formatter = logging.Formatter ('%(name)s - %(levelname)s - %(message)s')
stream_h.setFormatter(formatter) #instead of individual setting for each handler, we can assign it to a variable and refrence it that way
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('This is a warning log message')
logger.error("This is an error log message")



