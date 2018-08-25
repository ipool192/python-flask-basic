from app.infrastructures.sql_connector import connect
from app.logger import logger

def get_user_by_id_or_email(id_or_email, *selectField):
    connection = connect()
    if connection is None:
        return dict(
            error = True,
            message = "Failed connection"
        )
    try:
        with connection.cursor() as cursor:
            fieldQuery = ", ".join(selectField) if len(selectField) > 0 else "*"
            sql = "SELECT "+fieldQuery+" FROM users WHERE (id = %s OR email = %s)"
            cursor.execute(sql, (id_or_email, id_or_email, ))
            result = cursor.fetchone()
            
            if result is None:
                return dict(
                    message = "User not found",
                    error = True
                )
            return dict(
                data = result,
                error = False
            )
    except Exception as error:
        logger.error(str(error))
        return dict(
            message = str(error),
            error = True
        )
    finally:
        connection.close()