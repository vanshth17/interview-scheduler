import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MODEL_NAME = os.getenv("MODEL_NAME", "llama3")
    DB_PATH = os.getenv("DB_PATH", "interviews.db")
    ENV = os.getenv("ENV", "development")

settings = Settings()