# =================================================
# MICRO & MACRO ECONOMICS PLATFORM
# Real-time classroom competition version
# Single-file professional app.py
# =================================================

import streamlit as st
import numpy as np
import pandas as pd
import random
import time

# database functions
from database import init_db, save_score, get_scores

init_db()
if "competition_active" not in st.session_state:
    st.session_state.competition_active = False

if "current_question" not in st.session_state:
    st.session_state.current_question = None

if "question_duration" not in st.session_state:
    st.session_state.question_duration = 20

if "question_start_time" not in st.session_state:
    st.session_state.question_start_time = 0

# =================================================
# PAGE CONFIG
# =================================================

st.set_page_config(
    page_title="Economics Classroom Platform",
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
# LANGUAGE
# =================================================

lang = st.sidebar.selectbox(
    "Language",
    ["English", "العربية"]
)

# =================================================
# TEXT LABELS
# =================================================

TEXT = {

"title": {
"English": "Economics Classroom Platform",
"العربية": "منصة الاقتصاد التعليمية"
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
"English": "Practice Quiz",
"العربية": "اختبار تدريبي"
},

"competition": {
"English": "Live Classroom Competition",
"العربية": "مسابقة الصف المباشرة"
}

}
# =================================================
# PAGE NAVIGATION
# =================================================

page = st.sidebar.selectbox(
    "Select Page" if lang == "English" else "اختر الصفحة",
    [
        "Simulation",
        "Quiz",
        "Competition",
        "Teacher Control Panel"
    ]
)

# =================================================
# TITLE
# =================================================

st.title(TEXT["title"][lang])

# =================================================
# NAVIGATION
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
# DEMAND SUPPLY MODULE
# =================================================

if page == TEXT["demand_supply"][lang]:

    st.header(TEXT["demand_supply"][lang])

    col1, col2 = st.columns(2)

    with col1:

        a = st.slider("Demand intercept", 50, 200, 120)
        b = st.slider("Demand slope", 1, 10, 3)

    with col2:

        c = st.slider("Supply intercept", 0, 100, 20)
        d = st.slider("Supply slope", 1, 10, 2)

    eq_price = (a-c)/(b+d)
    eq_quantity = a - b*eq_price

    st.success(
        f"Equilibrium Price = {eq_price:.2f} | Quantity = {eq_quantity:.2f}"
    )

    prices = np.linspace(0, eq_price*2, 50)

    demand = a - b*prices
    supply = c + d*prices

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

    Q1 = st.slider("Initial Quantity", 10, 200, 100)
    Q2 = st.slider("New Quantity", 10, 200, 70)

    elasticity = (

        ((Q2-Q1)/((Q1+Q2)/2)) /
        ((P2-P1)/((P1+P2)/2))

    )

    st.metric("Elasticity", round(elasticity,2))

# =================================================
# PRACTICE QUIZ MODULE
# =================================================

elif page == TEXT["quiz"][lang]:

    st.header(TEXT["quiz"][lang])

    if "practice_score" not in st.session_state:
        st.session_state.practice_score = 0

    q = random.choice([

        ("Elastic demand means elasticity is:", ">1"),
        ("Inelastic demand means elasticity is:", "<1"),
        ("Unit elastic demand means elasticity equals:", "=1")

    ])

    answer = st.radio(q[0], [">1", "<1", "=1"])

    if st.button("Submit Answer"):

        if answer == q[1]:

            st.success("Correct")
            st.session_state.practice_score += 1

        else:

            st.error("Incorrect")

    st.write("Score:", st.session_state.practice_score)

# =================================================
# LIVE CLASSROOM COMPETITION
# =================================================

elif page == TEXT["competition"][lang]:

    st.header(TEXT["competition"][lang])

    col1, col2 = st.columns(2)

    with col1:

        classroom = st.text_input("Classroom Code")

        player = st.text_input("Student Name")

    with col2:

        if "competition_score" not in st.session_state:
            st.session_state.competition_score = 0

        if "question_id" not in st.session_state:
            st.session_state.question_id = 1

    # -----------------------------------
    # GENERATE LIVE QUESTION
    # -----------------------------------

    questions = [

        {
            "q": "If elasticity > 1, demand is:",
            "options": ["Elastic", "Inelastic", "Unit Elastic"],
            "answer": "Elastic"
        },

        {
            "q": "If elasticity < 1, demand is:",
            "options": ["Elastic", "Inelastic", "Unit Elastic"],
            "answer": "Inelastic"
        },

        {
            "q": "If elasticity = 1, demand is:",
            "options": ["Elastic", "Inelastic", "Unit Elastic"],
            "answer": "Unit Elastic"
        }

    ]

    current_question = random.choice(questions)

    st.subheader(f"Question {st.session_state.question_id}")

    answer = st.radio(
        current_question["q"],
        current_question["options"]
    )

    colA, colB = st.columns(2)

    # -----------------------------------
    # SUBMIT ANSWER
    # -----------------------------------

    with colA:

        if st.button("Submit"):

            if answer == current_question["answer"]:

                st.success("Correct!")
                st.session_state.competition_score += 10

            else:

                st.error("Wrong!")

            st.session_state.question_id += 1

    # -----------------------------------
    # SAVE SCORE
    # -----------------------------------

    with colB:

        if st.button("Save to Leaderboard"):

            if classroom and player:

                save_score(
                    classroom,
                    player,
                    st.session_state.competition_score
                )

                st.success("Saved!")

    # -----------------------------------
    # DISPLAY SCORE
    # -----------------------------------

    st.metric(
        "Your Score",
        st.session_state.competition_score
    )

    # -----------------------------------
    # LIVE LEADERBOARD
    # -----------------------------------

    if classroom:

        st.subheader("Live Leaderboard")

        scores = get_scores(classroom)

        if scores:

            df = pd.DataFrame(
                scores,
                columns=["Student", "Score"]
            )

            df = df.sort_values(
                "Score",
                ascending=False
            )

            st.table(df)

    # -----------------------------------
    # AUTO REFRESH
    # -----------------------------------

    time.sleep(1)
    st.rerun()

if st.button("Reset Competition" if lang == "English" else "إعادة تعيين المسابقة"):
    st.session_state.leaderboard = {}
    st.session_state.score = 0
    st.session_state.question_number = 1


# =================================================
# TEACHER CONTROL PANEL  ← ADD HERE
# =================================================

if page == "Teacher Control Panel":

    st.header("Teacher Control Panel")

    password = st.text_input(
        "Enter Teacher Password",
        type="password"
    )

    if password == "admin123":

        st.success("Teacher mode activated")

        duration = st.slider(
            "Question duration (seconds)",
            5,
            60,
            20
        )

        st.session_state.question_duration = duration

        if st.button("Start Competition"):

            st.session_state.competition_active = True

            st.session_state.current_question = generate_question()

            st.session_state.question_start_time = time.time()

        if st.button("Stop Competition"):

            st.session_state.competition_active = False

        if st.button("Next Question"):

            st.session_state.current_question = generate_question()

            st.session_state.question_start_time = time.time()

        if st.session_state.current_question:

            st.write(
                st.session_state.current_question["question"]
            )

    else:

        st.warning("Enter correct password")

