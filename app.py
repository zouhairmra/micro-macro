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
        economic_context = f"""
        MARKET DATA
        ------------------
        Demand intercept (a): {a}
        Demand slope (b): {b_el}

        Equilibrium price: {eq_price}
        Equilibrium quantity: {eq_quantity}

        Current price: {price}

        Quantity demanded: {Qd_val}
        Quantity supplied: {Qs_val}

        Market status: {market_status}

        ELASTICITY DATA
        ------------------
        Initial price: {P1}
        New price: {P2}

        Quantity initial: {Q1}
        Quantity new: {Q2}

        Price elasticity: {elasticity}
        Elasticity type: {elasticity_type}

        Total revenue initial: {TR1}
        Total revenue new: {TR2}

        CROSS ELASTICITY
        ------------------
        Cross elasticity: {cross_elasticity}
        Relationship: {cross_type}

        INCOME ELASTICITY
        ------------------
        Income elasticity: {income_elasticity}
        Good type: {income_type}
        """

        system_prompt = """
        You are an expert economics professor and economic consultant.

        Your job is to:

        - Analyze demand and supply
        - Interpret elasticity
        - Explain equilibrium
        - Give managerial pricing recommendations
        - Explain revenue effects
        - Explain substitutes/complements
        - Explain normal/inferior/luxury goods

        Give clear, structured explanation suitable for university students.
        """

        user_prompt = f"""
        Economic simulation data:

        {economic_context}

        Student question:

        {student_question}

        Provide:

        1. Explanation
        2. Economic interpretation
        3. Managerial recommendation
        """

        with st.spinner(
            "AI analyzing..."
            if lang == "English"
            else "الذكاء الاصطناعي يحلل..."
        ):

            response = client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],

                temperature=0.3
            )

            ai_answer = response.choices[0].message.content

        st.success(
            "AI Economic Analysis"
            if lang == "English"
            else "تحليل الذكاء الاصطناعي"
        )

        st.write(ai_answer)
