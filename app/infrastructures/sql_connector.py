import pymysql
import os
from app.logger import logger

def connect():
    try:
        connection = pymysql.connect(
            host = os.getenv("READ_HOST"),
            port = os.getenv("READ_PORT"),
            user = os.getenv("READ_USERNAME"),
            password = os.getenv("READ_PASSWORD"),
            db = os.getenv("READ_DATABASE"),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except Exception as error:
        logger.error(str(error))
        return None