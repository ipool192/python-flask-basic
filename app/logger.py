import logging
from logging.handlers import RotatingFileHandler
import os

logger = logging.getLogger(__name__)
handler = RotatingFileHandler(
    os.getenv('ERR_LOG_LOCATION'),
    maxBytes=os.getenv('ERR_LOG_MAXBYTES'),
    backupCount=os.getenv('ERR_LOG_BACKUP_COUNT')
)
handler.setLevel(logging._checkLevel(os.getenv('ERR_LOG_LEVEL')))
handler.setFormatter(
    logging.Formatter('%(asctime)s [%(levelname)s] %(message)s %(pathname)s:%(lineno)d')
)
logger.addHandler(handler)
