import os
from dotenv import load_dotenv

# Load from .env file (if present)
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")

    # MySQL Config
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_NAME = os.getenv("DB_NAME", "kanban_db")
