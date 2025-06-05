import streamlit as st
from utils import get_bot_response, get_triage_level, run_symptom_checker

# Page settings
st.set_page_config(page_title="Health AI Assistant", page_icon="🩺", layout="centered")
st.markdown(
    """
    <style>
    .main { background-color: #f0f2f6; }
    .stButton > button {
        color: white;
        background-color: #4CAF50;
        font-size: 16px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stTextInput > div > div > input {
        font-size: 18px;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🩺 Health Chatbot")
st.caption("Your AI-powered health assistant (Not a substitute for professional medical advice).")

with st.expander("ℹ️ **How it works**"):
    st.markdown("""
    This chatbot uses the **DeepSeek R1** AI model via OpenRouter to:
    - 🧠 Answer health-related questions.
    - 🚦 Assess the urgency of your symptoms.
    - 💡 Suggest possible causes and advice.

    This is an experimental tool — please consult a real doctor for any medical concerns.
    """)

# Input field
st.markdown("### ❓ What would you like to ask or describe?")
user_input = st.text_input("Type your symptoms or question here", placeholder="e.g., I have a sore throat and fever")

# Button to trigger AI response
if st.button("💬 Get AI Response"):
    if user_input:
        with st.spinner("Thinking... Please wait a few seconds..."):
            try:
                reply = get_bot_response(user_input)
                triage = get_triage_level(user_input)
                assessment = run_symptom_checker(user_input)
            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
                st.stop()

        st.markdown("### 🤖 AI Response")
        st.success(reply)

        st.markdown("### 🚦 Triage Level")
        if "low" in triage:
            st.info("🟢 Urgency: **Low** — Monitor your symptoms at home.")
        elif "medium" in triage:
            st.warning("🟠 Urgency: **Medium** — Consider seeing a doctor soon.")
        elif "high" in triage:
            st.error("🔴 Urgency: **High** — Seek **immediate** medical attention.")
        else:
            st.write(f"⚠️ Could not determine urgency: {triage}")

        st.markdown("### 🩺 Symptom Analysis")
        st.write(assessment)
    else:
        st.warning("Please enter some symptoms or a question above.")
