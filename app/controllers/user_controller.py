from app.models.user import get_user_by_id_or_email
from app.libraries.api_helper import response

class UserController(object):
    def get_user(self, id_user):
        try:
            # get user by id
            res = get_user_by_id_or_email(id_user, "id", "first_name", "last_name", "email")
            
            if res['error']:
                return response(1003, res['message'])
            else:
                return response(200, res['data'])
        except Exception as error:
            return response(1008, str(error))