# ================================================= 
# ECONOMICS PLATFORM — MAIN APP
# With AI Chatbot Integration
# =================================================

import streamlit as st
import time
import requests
import pandas as pd

# Modules
from config import get_text
from modules import demand_supply, elasticity, quiz, competition, teacher_panel, chatbot,

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
}

# Chatbot page
chatbot_page_name = "Chatbot" if lang == "English" else "المساعد"
page_options = list(pages.keys()) + [chatbot_page_name]

page_choice = st.sidebar.radio(
    get_text("navigation", lang),
    page_options
)

# =================================================
# RUN SELECTED MODULE OR CHATBOT
# =================================================

if page_choice in pages:
    # Run normal module
    pages[page_choice].run(lang)

else:
    # ==========================
    # CHATBOT PAGE
    # ==========================
    st.header("🤖 Economics Chatbot" if lang == "English" else "🤖 المساعد الاقتصادي الذكي")
    st.write(
        "Ask anything about economics or your results."
        if lang == "English"
        else "اسأل أي شيء عن الاقتصاد أو نتائجك"
    )

    # API Key input
    POE_API_KEY = st.text_input(
        "Enter your Poe API Key (optional)" if lang == "English" else "أدخل مفتاح Poe (اختياري)",
        type="password"
    )

    user_input = st.text_input(
        "Type your question..." if lang == "English" else "اكتب سؤالك هنا..."
    )

    if user_input:
        st.session_state["chat_messages"].append({"role": "user", "content": user_input})

        with st.spinner("Generating response..." if lang == "English" else "جاري إنشاء الرد..."):
            if POE_API_KEY:
                try:
                    POE_API_URL = "https://api.poe.com/v1/chat/completions"
                    MODEL = "gpt-4o-mini"

                    headers = {
                        "Authorization": f"Bearer {POE_API_KEY}",
                        "Content-Type": "application/json"
                    }
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

            else:
                assistant_response = "Please enter a Poe API key to get AI responses." \
                    if lang == "English" else "الرجاء إدخال مفتاح Poe للحصول على ردود الذكاء الاصطناعي."

        st.session_state["chat_messages"].append({"role": "assistant", "content": assistant_response})

    # Display chat messages
    for msg in st.session_state["chat_messages"]:
        role = "User" if msg["role"] == "user" else "Assistant"
        st.markdown(f"**{role}:** {msg['content']}")

    # Clear chat button
    if st.button("🧹 Clear Chat" if lang == "English" else "مسح المحادثة"):
        st.session_state["chat_messages"] = []
        st.success("Chat cleared!" if lang == "English" else "تم مسح المحادثة!")

# =================================================
# FOOTER
# =================================================

st.markdown("---")
st.caption(
    "Economics Learning Platform" if lang == "English" else "منصة تعلم الاقتصاد"
)
