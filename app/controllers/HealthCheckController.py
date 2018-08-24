from app.libraries.api_helper import response

class HealthCheckController(object):
    def health_check(self):

        return response(200, "Success")
