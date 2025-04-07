import os
import requests
import logging

logger = logging.getLogger(__name__)

def gemini_generate(prompt: str) -> str:
    """
    Calls the Gemini API with the provided prompt and returns the generated text.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    api_url = os.getenv("GEMINI_API_URL", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent")
    
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": api_key
    }
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "maxOutputTokens": 512,
            "temperature": 0.7
        }
    }
    
    try:
        response = requests.post(api_url, headers=headers, params=params, json=payload)
        response.raise_for_status()
        data = response.json()
        generated_text = data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        return generated_text
    except Exception as e:
        logger.error("Error calling Gemini API", exc_info=True)
        return f"Error: {str(e)}"
