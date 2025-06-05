# 🩺 Health Chatbot with DeepSeek AI

An AI-powered health assistant built using [DeepSeek R1](https://openrouter.ai) and [Streamlit](https://streamlit.io/). This chatbot helps users:

- ✅ Get quick health advice (not a substitute for a doctor)
- 🚦 Classify urgency level of symptoms
- 🧠 Understand possible causes and suggestions

## 🚀 Demo

🔗 [Try it live on Streamlit →](https://chatbotforhealth.streamlit.app/)

## 💡 Features

- Natural language health Q&A
- Triage level classification (low, medium, high)
- Symptom analysis & suggestions
- Built with `requests`, `Streamlit`, and `DeepSeek-R1` via OpenRouter API

## 🔧 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/babiku42/health-chatbot.git
cd health-chatbot

# Install dependencies
pip install -r requirements.txt

# Set up your environment variables
Create a .env file based on .env.example:


# Run the app
streamlit run app.py
