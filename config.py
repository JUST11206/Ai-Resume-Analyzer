import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    UPLOAD_FOLDER = "uploads"

    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    ALLOWED_EXTENSIONS = {"pdf"}