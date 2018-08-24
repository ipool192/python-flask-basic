from app import app 
from app import configurations 
import os

if __name__ == "__main__":
    app.run(
        host = os.getenv("APP_HOST"),
        port = os.getenv("APP_PORT")
    )