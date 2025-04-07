import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Retrieve the API key and model name from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_MODEL = os.getenv("GEMINI_API_MODEL", "gemini-2.0-flash")

if not GEMINI_API_KEY:
    logger.error("GEMINI_API_KEY is not set in the environment.")

# Configure the Gemini API using only the API key
genai.configure(api_key=GEMINI_API_KEY)

# Instantiate the model using the model name
model = genai.GenerativeModel(GEMINI_API_MODEL)

def gemini_generate(prompt: str) -> str:
    """
    Calls the Gemini API using the provided prompt and returns the generated text.
    This function uses only the API key and model name from the environment.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        logger.error("Error calling Gemini API", exc_info=True)
        return f"Error: {str(e)}"
