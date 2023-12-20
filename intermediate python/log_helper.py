import logging
#its good practice to create your own logger just like this one
logger = logging.getLogger(__name__) #this creates a logger with the name of the module or file, in this case: log_helper
logger.info ('Logger from module created by Samuel')

