# =================================================
# ECONOMICS PLATFORM — MAIN APP
# Clean Professional Version with AI Assistant
# =================================================

import streamlit as st
import time

# Modules
from config import get_text
from modules import demand_supply, elasticity, quiz, competition, teacher_panel, chatbot

# Optional OpenAI
try:
    from openai import OpenAI
except:
    OpenAI = None


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
# AI SETTINGS (OPTIONAL)
# =================================================

st.sidebar.markdown("---")

st.sidebar.subheader(
    "AI Economics Assistant"
    if lang == "English"
    else "المساعد الاقتصادي الذكي"
)

api_key = st.sidebar.text_input(
    "Enter OpenAI API Key (optional)"
    if lang == "English"
    else "أدخل مفتاح OpenAI (اختياري)",
    type="password"
)

ai_enabled = False
client = None

if api_key and OpenAI:
    try:
        client = OpenAI(api_key=api_key)
        ai_enabled = True
    except:
        ai_enabled = False


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
# INTELLIGENT AI ECONOMICS ASSISTANT
# =================================================

st.markdown("---")

st.header(
    "Intelligent Economics AI Tutor"
    if lang == "English"
    else "المعلم الاقتصادي الذكي"
)

st.write(
    "Analyze elasticity, equilibrium, revenue, and market results."
    if lang == "English"
    else "تحليل المرونة والتوازن والإيرادات ونتائج السوق."
)

student_question = st.text_area(

    "Ask about YOUR results or economics concepts:"
    if lang == "English"
    else "اسأل عن نتائجك أو مفاهيم الاقتصاد:"

)


if st.button(

    "Analyze Economic Situation"
    if lang == "English"
    else "تحليل الوضع الاقتصادي"

):

    econ = st.session_state.get("economic_data", {})

    price = econ.get("price", None)
    quantity = econ.get("quantity", None)
    elasticity_val = econ.get("elasticity", None)
    revenue = econ.get("revenue", None)
    intercept = econ.get("intercept", None)
    slope = econ.get("slope", None)

    context = f"""
Student Data:

Price: {price}
Quantity: {quantity}
Elasticity: {elasticity_val}
Revenue: {revenue}
Demand intercept: {intercept}
Demand slope: {slope}

Question:
{student_question}
"""


    # =================================================
    # OPENAI VERSION
    # =================================================

    if ai_enabled:

        try:

            response = client.chat.completions.create(

                model="gpt-4o-mini",

                messages=[

                    {
                        "role": "system",
                        "content": """
You are an expert economics professor.

Explain elasticity, equilibrium, and revenue clearly.

Give managerial advice.
"""
                    },

                    {
                        "role": "user",
                        "content": context
                    }

                ],

                temperature=0.2,

                max_tokens=400

            )

            answer = response.choices[0].message.content

            st.success(answer)


        except Exception as e:

            st.warning(
                "API quota exceeded. Using internal AI engine instead."
                if lang == "English"
                else "تم تجاوز الحصة. استخدام الذكاء الداخلي."
            )

            ai_enabled = False


    # =================================================
    # INTERNAL ECONOMIC AI ENGINE (ALWAYS AVAILABLE)
    # =================================================

    if not ai_enabled:

        if elasticity_val is not None:

            if elasticity_val > 1:

                st.success(f"""

Elasticity = {elasticity_val:.2f} → ELASTIC DEMAND

Managerial Recommendation:

• Lower price to increase total revenue  
• Consumers are price sensitive  

""")

            elif elasticity_val < 1:

                st.success(f"""

Elasticity = {elasticity_val:.2f} → INELASTIC DEMAND

Managerial Recommendation:

• Increase price to increase revenue  
• Consumers are less sensitive  

""")

            else:

                st.success("""

Unit Elastic Demand

Revenue is maximized at this point.

""")


        else:

            st.info(

                "Run Elasticity or Demand-Supply module first."
                if lang == "English"
                else "قم بتشغيل وحدة المرونة أو العرض والطلب أولاً."

            )


# =================================================
# FOOTER
# =================================================

st.markdown("---")

st.caption(

    "AI-Powered Economics Learning Platform"
    if lang == "English"
    else "منصة تعلم الاقتصاد المدعومة بالذكاء الاصطناعي"

)
