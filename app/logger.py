import logging
from logging.handlers import RotatingFileHandler
from app.libraries.environment import envInt, envString

logger = logging.getLogger(__name__)
handler = RotatingFileHandler(
    envString('ERR_LOG_LOCATION'),
    maxBytes=envInt('ERR_LOG_MAXBYTES'),
    backupCount=envInt('ERR_LOG_BACKUP_COUNT')
)
handler.setLevel(logging._checkLevel(envString('ERR_LOG_LEVEL')))
handler.setFormatter(
    logging.Formatter('%(asctime)s [%(levelname)s] %(message)s %(pathname)s:%(lineno)d')
)
logger.addHandler(handler)
