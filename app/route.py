from app import app
from app.libraries.api_helper import response
from app.controllers.healthcheck_controller import HealthCheckController
from app.controllers.user_controller import UserController

# Router Error #
@app.errorhandler(400)
def bad_request(error):
    return response(400, "The browser (or proxy) sent a request that this server could not understand."), 400

@app.errorhandler(405)
def method_not_allowed(error):
    return response(405, "The method is not allowed for the requested URL."), 405

@app.errorhandler(404)
def page_not_found(error):
    return response(404, "Halaman yang Anda minta tidak tersedia."), 400

@app.errorhandler(403)
def forbidden_error(error):
    return response(403, "Anda tidak memiliki akses."), 403

@app.errorhandler(410)
def unauthorized_eror(error):
    return response(410, "Anda tidak memiliki akses."), 410

@app.errorhandler(500)
def internal_server_error(error):
    return response(500, "Terjadi masalah pada server."), 500
# End Router Error #

@app.route("/v1/healthcheck", methods=["GET"])
def healthcheck():
    return HealthCheckController().health_check()

@app.route("/v1/user/<int:id_user>", methods=["GET"])
def get_user(id_user):
    return UserController().get_user(id_user)