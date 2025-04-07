# config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Gemini API configurations
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://api.gemini.example.com/v1/generate")

# You can add additional configuration variables here as needed.
