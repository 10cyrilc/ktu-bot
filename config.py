import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    MONGO_URI = os.getenv("MONGO_URI")
    SESSION_NAME = os.getenv("SESSION_NAME")
    BOT_ID = os.getenv("BOT_ID")
