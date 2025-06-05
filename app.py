import streamlit as st
from utils import get_bot_response, get_triage_level, run_symptom_checker

st.set_page_config(page_title="Health AI Assistant", page_icon="🩺", layout="wide")

# --- HEADER SECTION ---
st.markdown(
    """
    <style>
    .header {
        text-align: center;
        color: #117A65;
        font-size: 48px;
        font-weight: 700;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        margin-bottom: 0;
    }
    .subheader {
        text-align: center;
        color: #148F77;
        font-size: 22px;
        font-style: italic;
        margin-top: 0;
        margin-bottom: 30px;
    }
    .footer {
        color: #aaa;
        font-size: 12px;
        text-align: center;
        margin-top: 50px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="header">🩺 Health AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Your AI-powered companion for health advice and symptom checking</p>', unsafe_allow_html=True)

# --- LAYOUT: two columns ---
col1, col2 = st.columns([2, 1])

with col1:
    # Input section
    user_input = st.text_area("Enter your symptoms or questions here:", height=130, placeholder="e.g., I have a headache and fever...")

    if st.button("Get Response"):
        if user_input.strip():
            with st.spinner("🤖 Analyzing your symptoms... Please wait."):
                # Get AI responses
                reply = get_bot_response(user_input)
                triage = get_triage_level(user_input)
                assessment = run_symptom_checker(user_input)

            # Display chatbot response
            st.markdown("### 🤖 AI Response")
            st.success(reply)

            st.markdown("### 🚦 Triage Level")
            if "low" in triage:
                st.info("Urgency: **Low** — Monitor your symptoms.")
            elif "medium" in triage:
                st.warning("Urgency: **Medium** — Consider seeing a doctor.")
            elif "high" in triage:
                st.error("Urgency: **High** — Seek medical attention immediately.")
            else:
                st.write(triage)

            st.markdown("### 🩻 Symptom Analysis")
            st.write(assessment)
        else:
            st.warning("Please enter some symptoms or a question.")

with col2:
    st.markdown("### 💡 Tips for best results:")
    st.markdown(
        """
        - Describe symptoms clearly and briefly.
        - Include duration and severity.
        - Avoid medical jargon for best AI understanding.
        - Remember, this tool is **not a substitute for professional medical advice**.
        """
    )
    st.image(
        "https://digital.nls.uk/great-war/assets/img/content/general/pic-casualties-4-large.gif?auto=format&fit=crop&w=400&q=60",
        caption="Stay healthy! 💙",
        use_column_width=True,
    )

# --- FOOTER ---
st.markdown('<div class="footer">Developed by BIKASH ADHIKARI | Powered by OpenAI and DeepSeek AI Models</div>', unsafe_allow_html=True)
