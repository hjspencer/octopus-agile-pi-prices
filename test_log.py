from datetime import datetime
import logging

# find current time and convert to year month day etc
the_now_local = datetime.now()

log_file_name = 'logfile_' + str(the_now_local.year) + str(the_now_local.month) + str(the_now_local.day) + '.log'

logger = logging.getLogger(__name__) 
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(log_file_name)
formatter    = logging.Formatter('%(asctime)s : %(levelname)-8s : %(filename)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Logs
logger.debug('A debug message')
logger.info('An info message')
logger.warning('Something is not right.')
logger.error('A Major error has happened.')
logger.critical('Fatal error. Cannot continue')