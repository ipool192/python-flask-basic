import pymysql
from app.libraries.environment import envString, envInt
from app.logger import logger

def connect():
    try:
        connection = pymysql.connect(
            host = envString("DB_HOST"),
            port = envInt("DB_PORT"),
            user = envString("DB_USERNAME"),
            password = envString("DB_PASSWORD"),
            db = envString("DB_DATABASE"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as error:
        logger.error(str(error))
        return None