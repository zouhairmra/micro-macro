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
       # ===============================
# AI ECONOMICS ASSISTANT
# ===============================

st.markdown("---")
st.header("AI Economics Assistant")

user_question = st.text_area(
    "Ask any question about elasticity, microeconomics, macroeconomics, or your results:"
)

if st.button("Ask AI Assistant"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")
    else:

        # Safely retrieve variables if they exist
        a_val = globals().get("a", None)
        b_val = globals().get("b", None)
        P_val = globals().get("P", None)
        Q_val = globals().get("Q", None)
        elasticity_val = globals().get("elasticity", None)

        # Build economic context safely
        context = f"""
        Student economic model:

        Demand intercept (a): {a_val if a_val is not None else "Not defined"}
        Demand slope (b): {b_val if b_val is not None else "Not defined"}
        Price (P): {P_val if P_val is not None else "Not defined"}
        Quantity (Q): {Q_val if Q_val is not None else "Not defined"}
        Elasticity: {elasticity_val if elasticity_val is not None else "Not defined"}

        Student question:
        {user_question}
        """

        # Simple built-in AI logic (no OpenAI dependency)
        if "elasticity" in user_question.lower():
            response = """
Elasticity measures responsiveness of quantity demanded to price changes.

If elasticity > 1 → Elastic demand  
If elasticity = 1 → Unit elastic  
If elasticity < 1 → Inelastic demand  

Elastic demand means consumers are sensitive to price changes.
"""
        elif "demand" in user_question.lower():
            response = """
Demand shows the relationship between price and quantity demanded.

Law of demand: when price increases, quantity demanded decreases.
"""
        elif "supply" in user_question.lower():
            response = """
Supply shows the relationship between price and quantity supplied.

Law of supply: when price increases, quantity supplied increases.
"""
        else:
            response = f"""
Your question: "{user_question}"

Economic interpretation:
This relates to decision-making, optimization, and market behavior.
Consider analyzing elasticity, marginal effects, and equilibrium.
"""

        st.success(response)
