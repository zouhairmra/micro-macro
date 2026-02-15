import streamlit as st
from config import get_text
from modules import demand_supply, elasticity, quiz, competition, teacher_panel, chatbot
from openai import OpenAI
import time

# =================================================
# PAGE CONFIG
# =================================================
st.set_page_config(page_title="Economics Platform", layout="wide")

# =================================================
# LANGUAGE SELECTION
# =================================================
lang = st.sidebar.selectbox("Language", ["English", "العربية"])
# =================================================
# AI ASSISTANT SETTINGS
# =================================================

st.sidebar.subheader(
    "AI Economics Assistant"
    if lang == "English"
    else "المساعد الاقتصادي الذكي"
)

api_key = st.sidebar.text_input(
    "Enter OpenAI API Key"
    if lang == "English"
    else "أدخل مفتاح OpenAI",
    type="password"
)

ai_enabled = api_key != ""

if ai_enabled:
    client = OpenAI(api_key=api_key)

# =================================================
# PAGE NAVIGATION
# =================================================
pages = {
    get_text("demand_supply", lang): demand_supply,
    get_text("elasticity", lang): elasticity,
    get_text("quiz", lang): quiz,
    get_text("competition", lang): competition,  # Competition améliorée avec chatbot intégré
    get_text("teacher_panel", lang): teacher_panel,
    get_text("chatbot", lang): chatbot  # Chatbot autonome
}

page_choice = st.sidebar.radio(get_text("navigation", lang), list(pages.keys()))

# =================================================
# RUN SELECTED MODULE
# =================================================
pages[page_choice].run(lang)
# =================================================
# FULL AI ECONOMICS ASSISTANT
# =================================================

st.header(
    "AI Economics Assistant"
    if lang == "English"
    else "المساعد الاقتصادي الذكي"
)

st.write(
    "Ask the AI to analyze equilibrium, elasticity, revenue, or market conditions."
    if lang == "English"
    else "اطلب من الذكاء الاصطناعي تحليل التوازن أو المرونة أو الإيرادات أو حالة السوق."
)

student_question = st.text_area(
    "Your question:"
    if lang == "English"
    else "سؤالك:"
)

if st.button(
    "Analyze Economic Situation"
    if lang == "English"
    else "تحليل الوضع الاقتصادي"
):

    if not ai_enabled:

        st.warning(
            "Please enter OpenAI API key in sidebar"
            if lang == "English"
            else "يرجى إدخال مفتاح OpenAI"
        )

    else:

        # FULL ECONOMIC CONTEXT FROM SIMULATION
       # SAFE VARIABLE EXTRACTION

a_val = globals().get("a", "Not defined")
b_val = globals().get("b_el", "Not defined")
eq_price_val = globals().get("eq_price", "Not defined")
eq_quantity_val = globals().get("eq_quantity", "Not defined")
price_val = globals().get("price", "Not defined")
Qd_val_safe = globals().get("Qd_val", "Not defined")
Qs_val_safe = globals().get("Qs_val", "Not defined")
market_status_val = globals().get("market_status", "Not defined")

elasticity_val = globals().get("elasticity", "Not defined")
elasticity_type_val = globals().get("elasticity_type", "Not defined")
TR1_val = globals().get("TR1", "Not defined")
TR2_val = globals().get("TR2", "Not defined")

cross_elasticity_val = globals().get("cross_elasticity", "Not defined")
cross_type_val = globals().get("cross_type", "Not defined")

income_elasticity_val = globals().get("income_elasticity", "Not defined")
income_type_val = globals().get("income_type", "Not defined")

economic_context = f"""
MARKET DATA
------------------
Demand intercept (a): {a_val}
Demand slope (b): {b_val}

Equilibrium price: {eq_price_val}
Equilibrium quantity: {eq_quantity_val}

Current price: {price_val}

Quantity demanded: {Qd_val_safe}
Quantity supplied: {Qs_val_safe}

Market status: {market_status_val}

ELASTICITY DATA
------------------
Price elasticity: {elasticity_val}
Elasticity type: {elasticity_type_val}

Total revenue initial: {TR1_val}
Total revenue new: {TR2_val}

CROSS ELASTICITY
------------------
Cross elasticity: {cross_elasticity_val}
Relationship: {cross_type_val}

INCOME ELASTICITY
------------------
Income elasticity: {income_elasticity_val}
Good type: {income_type_val}
"""
