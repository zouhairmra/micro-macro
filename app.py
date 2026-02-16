# =================================================
# MICRO & MACRO ECONOMICS PLATFORM
# Professional organized version (single-file)
# =================================================

import streamlit as st
import numpy as np
import pandas as pd
import random

# Database
from database import init_db, save_score, get_scores

# Initialize database
init_db()

# =================================================
# PAGE CONFIGURATION
# =================================================

st.set_page_config(
    page_title="Micro & Macro Economics Platform",
    layout="wide"
)

# =================================================
# LOAD CSS
# =================================================

def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except:
        pass

load_css()

# =================================================
# LANGUAGE SELECTION
# =================================================

lang = st.sidebar.selectbox(
    "Language",
    ["English", "العربية"]
)

# Labels dictionary
TEXT = {

    "title": {
        "English": "Micro & Macro Economics Platform",
        "العربية": "منصة الاقتصاد الجزئي والكلي"
    },

    "navigation": {
        "English": "Navigation",
        "العربية": "التنقل"
    },

    "demand_supply": {
        "English": "Demand & Supply",
        "العربية": "العرض والطلب"
    },

    "elasticity": {
        "English": "Elasticity",
        "العربية": "المرونة"
    },

    "quiz": {
        "English": "Quiz",
        "العربية": "اختبار"
    },

    "competition": {
        "English": "Competition",
        "العربية": "مسابقة"
    }

}

# =================================================
# TITLE
# =================================================

st.title(TEXT["title"][lang])

# =================================================
# NAVIGATION MENU
# =================================================

page = st.sidebar.radio(
    TEXT["navigation"][lang],
    [
        TEXT["demand_supply"][lang],
        TEXT["elasticity"][lang],
        TEXT["quiz"][lang],
        TEXT["competition"][lang]
    ]
)

# =================================================
# DEMAND & SUPPLY MODULE
# =================================================

if page == TEXT["demand_supply"][lang]:

    st.header(TEXT["demand_supply"][lang])

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Demand")

        a = st.slider("Intercept (a)", 50, 200, 120)
        b = st.slider("Slope (b)", 1, 10, 3)

    with col2:
        st.subheader("Supply")

        c = st.slider("Intercept (c)", 0, 100, 20)
        d = st.slider("Slope (d)", 1, 10, 2)

    eq_price = (a - c) / (b + d)
    eq_quantity = a - b * eq_price

    st.success(
        f"Equilibrium Price = {eq_price:.2f} | Quantity = {eq_quantity:.2f}"
    )

    # Graph
    prices = np.linspace(0, eq_price * 2, 50)

    demand = a - b * prices
    supply = c + d * prices

    df = pd.DataFrame({
        "Demand": demand,
        "Supply": supply
    }, index=prices)

    st.line_chart(df)

# =================================================
# ELASTICITY MODULE
# =================================================

elif page == TEXT["elasticity"][lang]:

    st.header(TEXT["elasticity"][lang])

    P1 = st.slider("Initial Price", 1, 100, 20)
    P2 = st.slider("New Price", 1, 100, 30)

    Q1 = st.slider("Initial Quantity", 1, 200, 100)
    Q2 = st.slider("New Quantity", 1, 200, 80)

    elasticity = (
        ((Q2 - Q1) / ((Q1 + Q2) / 2)) /
        ((P2 - P1) / ((P1 + P2) / 2))
    )

    TR1 = P1 * Q1
    TR2 = P2 * Q2

    st.metric("Elasticity", round(elasticity, 2))

    results = pd.DataFrame({

        "Price": [P1, P2],
        "Quantity": [Q1, Q2],
        "Revenue": [TR1, TR2]

    }, index=["Initial", "New"])

    st.table(results)

# =================================================
# QUIZ MODULE
# =================================================

elif page == TEXT["quiz"][lang]:

    st.header(TEXT["quiz"][lang])

    if "score" not in st.session_state:
        st.session_state.score = 0

    question = "Demand is elastic if elasticity is:"

    answer = st.radio(

        question,
        [
            "> 1",
            "< 1",
            "= 0"
        ]

    )

    if st.button("Submit"):

        if answer == "> 1":

            st.success("Correct")
            st.session_state.score += 1

        else:

            st.error("Incorrect")

    st.write("Score:", st.session_state.score)

# =================================================
# COMPETITION MODULE (MULTIPLAYER DATABASE)
# =================================================

elif page == TEXT["competition"][lang]:

    st.header(TEXT["competition"][lang])

    classroom = st.text_input("Classroom Code")

    player = st.text_input("Player Name")

    score = st.number_input("Score", 0, 100, 0)

    if st.button("Save Score"):

        if classroom and player:

            save_score(classroom, player, score)

            st.success("Score saved")

    if classroom:

        scores = get_scores(classroom)

        if scores:

            df = pd.DataFrame(

                scores,
                columns=["Player", "Score"]

            )

            st.subheader("Leaderboard")

            st.table(df)
