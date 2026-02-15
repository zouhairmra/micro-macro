# ================================================= 
# ECONOMICS PLATFORM — MAIN APP
# Clean Professional Version (AI Removed)
# =================================================

import streamlit as st
import time

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
    get_text("teacher_panel", lang): teacher_panel
}

page_choice = st.sidebar.radio(
    get_text("navigation", lang),
    list(pages.keys())
)

# =================================================
# RUN SELECTED MODULE
# =================================================

pages[page_choice].run(lang)

# =================================================
# FOOTER
# =================================================

st.markdown("---")

st.caption(
    "Economics Learning Platform"
    if lang == "English"
    else "منصة تعلم الاقتصاد"
)
