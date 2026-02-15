# ================================================= 
# ECONOMICS PLATFORM — MAIN APP
# AI CHATBOT INTEGRATION
# =================================================

import streamlit as st
import time
import requests
import pandas as pd

# Modules
from config import get_text
from modules import demand_supply, elasticity, quiz, competition, teacher_panel, chatbot

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Economics Platform",
    layout="wide"
)

# =================================================
# SESSION STATE INITIALIZATION
# =================================================

if "economic_data" not in st.session_state:
    st.session_state["economic_data"] = {}

if "competition_active" not in st.session_state:
    st.session_state["competition_active"] = False

# Chat memory
if "chat_messages" not in st.session_state:
    st.session_state["chat_messages"] = []

# =================================================
# LANGUAGE SELECTION
# =================================================

lang = st.sidebar.selectbox(
    "Language",
    ["English", "العربية"]
)

# =================================================
# PAGE NAVIGATION
# =================================================

pages = {
    get_text("demand_supply", lang): demand_supply,
    get_text("elasticity", lang): elasticity,
    get_text("quiz", lang): quiz,
    get_text("competition", lang): competition,
    get_text("teacher_panel", lang): teacher_panel,
    get_text("chatbot", lang): chatbot  # Chatbot page added
}

page_choice = st.sidebar.radio(
    get_text("navigation", lang),
    list(pages.keys())
)

# =================================================
# RUN SELECTED MODULE
# =================================================

if page_choice != get_text("chatbot", lang):
    # Run normal module
    pages[page_choice].run(lang)

else:
    # ==========================
    # CHATBOT PAGE
    # ==========================
    st.header("🤖 Economics Chatbot" if lang == "English" else "🤖 المساعد الاقتصادي الذكي")
    st.write("Ask anything about economics or your results." if lang == "English" else "اسأل أي شيء عن الاقتصاد أو نتائجك")

    # User input
    user_input = st.text_input(
        "Type your question..." if lang == "English" else "اكتب سؤالك هنا..."
    )

    if user_input:
        st.session_state["chat_messages"].append({"role": "user", "content": user_input})

        with st.spinner("Generating response..."):
            try:
                # Optional: Replace with your own API key & endpoint
                POE_API_URL = "https://api.poe.com/v1/chat/completions"
                POE_API_KEY = st.secrets.get("POE_API_KEY", "YOUR_POE_API_KEY_HERE")
                MODEL = "gpt-4o-mini"  # or "maztouriabot", "claude-3-haiku"

                headers = {"Authorization": f"Bearer {POE_API_KEY}", "Content-Type": "application/json"}
                payload = {
                    "model": MODEL,
                    "messages": [{"role": msg["role"], "content": msg["content"]} for msg in st.session_state["chat_messages"]]
                }

                res = requests.post(POE_API_URL, headers=headers, json=payload, timeout=60)
                res.raise_for_status()
                data = res.json()
                assistant_response = data["choices"][0]["message"]["content"]

            except Exception as e:
                assistant_response = f"Error fetching response: {e}"

        st.session_state["chat_messages"].append({"role": "assistant", "content": assistant_response})

    # Display chat messages
    for msg in st.session_state["chat_messages"]:
        role = "User" if msg["role"] == "user" else "Assistant"
        st.markdown(f"**{role}:** {msg['content']}")

    # Clear chat
    if st.button("🧹 Clear Chat"):
        st.session_state["chat_messages"] = []
        st.toast("Chat cleared!")

# =================================================
# FOOTER
# =================================================

st.markdown("---")

st.caption(
    "Economics Learning Platform" if lang == "English" else "منصة تعلم الاقتصاد"
)
