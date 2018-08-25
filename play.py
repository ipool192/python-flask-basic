from app import app
from app.libraries.environment import envInt, envString

if __name__ == "__main__":
    app.run(
        host = envString("APP_HOST"),
        port = envInt("APP_PORT")
    )