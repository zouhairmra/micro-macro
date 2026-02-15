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
    get_text("competition", lang): competition,
    get_text("teacher_panel", lang): teacher_panel,
    get_text("chatbot", lang): chatbot
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
# GLOBAL AI ECONOMICS ASSISTANT
# =================================================
st.markdown("---")

st.header(
    "AI Economics Assistant"
    if lang == "English"
    else "المساعد الاقتصادي الذكي"
)

student_question = st.text_area(
    "Ask about elasticity, equilibrium, demand, supply, revenue, GDP, inflation..."
    if lang == "English"
    else "اسأل عن المرونة أو التوازن أو الطلب أو العرض أو الناتج المحلي..."
)

if st.button(
    "Analyze"
    if lang == "English"
    else "تحليل"
):

    if student_question.strip() == "":
        st.warning(
            "Please enter a question"
            if lang == "English"
            else "يرجى إدخال سؤال"
        )

    else:

        # =====================================
        # GET ECONOMIC VARIABLES SAFELY
        # =====================================

        a_val = globals().get("a", None)
        b_val = globals().get("b", None)
        P_val = globals().get("P", None)
        Q_val = globals().get("Q", None)
        elasticity_val = globals().get("elasticity", None)

        context = f"""
        Economic simulation data:

        Demand intercept (a): {a_val}
        Demand slope (b): {b_val}
        Price: {P_val}
        Quantity: {Q_val}
        Elasticity: {elasticity_val}

        Student question:
        {student_question}
        """

        # =====================================
        # USE OPENAI IF AVAILABLE
        # =====================================

        if ai_enabled:

            try:

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": """
You are an expert economics professor.
Explain clearly using microeconomics and macroeconomics theory.
Use elasticity, equilibrium, revenue, GDP, inflation when relevant.
"""
                        },
                        {
                            "role": "user",
                            "content": context
                        }
                    ],
                    temperature=0.3
                )

                answer = response.choices[0].message.content

                st.success(answer)

            except Exception as e:

                st.error(f"AI Error: {e}")

        # =====================================
        # OFFLINE FALLBACK AI
        # =====================================

        else:

            question_lower = student_question.lower()

            if "elasticity" in question_lower:

                st.success("""
Elasticity measures responsiveness of quantity demanded to price changes.

Elastic (>1): very sensitive  
Inelastic (<1): not sensitive  
Unit (=1): proportional change
""")

            elif "equilibrium" in question_lower:

                st.success("""
Equilibrium occurs where demand equals supply.

At equilibrium:
• No shortage
• No surplus
• Market is stable
""")

            elif "demand" in question_lower:

                st.success("""
Law of demand:
When price increases, quantity demanded decreases.
""")

            elif "supply" in question_lower:

                st.success("""
Law of supply:
When price increases, quantity supplied increases.
""")

            else:

                st.success("""
This question relates to economic analysis.

Consider:
• elasticity
• equilibrium
• marginal analysis
• market structure
""")
