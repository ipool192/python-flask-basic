from app import configurations
import os

def envInt(key):
    return int(os.getenv(key))

def envString(key):
    return str(os.getenv(key))

def envBool(key):
    return True if os.getenv(key) == "True" else False