import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env if running locally
load_dotenv()

# Get your OpenRouter API key from environment variables
API_KEY = os.getenv("OPENROUTER_API_KEY")
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY environment variable is not set.")

# Headers and API endpoint
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://chatbotforhealth.streamlit.app",  # Optional but helps with usage ranking
    "X-Title": "Health Chatbot",  # Optional
}

API_URL = "https://openrouter.ai/api/v1/chat/completions"
MODEL_NAME = "deepseek/deepseek-r1-0528:free"


def _call_deepseek(messages):
    payload = {
        "model": MODEL_NAME,
        "messages": messages
    }
    response = requests.post(API_URL, headers=HEADERS, data=json.dumps(payload))
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def get_bot_response(user_input: str) -> str:
    messages = [
        {"role": "system", "content": "You are a helpful health assistant."},
        {"role": "user", "content": user_input}
    ]
    return _call_deepseek(messages)


def get_triage_level(symptoms: str) -> str:
    prompt = f"Classify the urgency of these symptoms: {symptoms}. Answer with: low, medium, or high."
    messages = [
        {"role": "system", "content": "Classify health symptoms into triage urgency levels."},
        {"role": "user", "content": prompt}
    ]
    return _call_deepseek(messages).strip().lower()


def run_symptom_checker(symptoms: str) -> str:
    prompt = f"The user reports: {symptoms}. What might be the cause? Should they see a doctor?"
    messages = [
        {"role": "system", "content": "You are a medical assistant."},
        {"role": "user", "content": prompt}
    ]
    return _call_deepseek(messages)
