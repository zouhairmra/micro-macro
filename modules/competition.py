import streamlit as st
import random
import time
from database import save_score, get_scores

def run(lang="English"):
    st.header("Live Classroom Competition" if lang=="English" else "مسابقة الصف المباشرة")

    col1, col2 = st.columns(2)

    with col1:
        classroom = st.text_input("Classroom Code" if lang=="English" else "رمز الصف")
        player = st.text_input("Student Name" if lang=="English" else "اسم الطالب")

    with col2:
        if "competition_score" not in st.session_state:
            st.session_state.competition_score = 0
        if "question_id" not in st.session_state:
            st.session_state.question_id = 1

    # Question bank
    questions = [
        {"q": "If elasticity > 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Elastic"},
        {"q": "If elasticity < 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"},
        {"q": "If elasticity = 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Unit Elastic"}
    ]

    # Current question
    if "current_question" not in st.session_state or st.session_state.current_question is None:
        st.session_state.current_question = random.choice(questions)

    q = st.session_state.current_question
    st.subheader(f"Question {st.session_state.question_id}")

    answer = st.radio(q["q"], q["options"])

    colA, colB = st.columns(2)

    with colA:
        if st.button("Submit" if lang=="English" else "إرسال"):
            if answer == q["answer"]:
                st.success("Correct!" if lang=="English" else "صحيح!")
                st.session_state.competition_score += 10
            else:
                st.error("Wrong!" if lang=="English" else "خطأ!")
            st.session_state.question_id += 1
            st.session_state.current_question = random.choice(questions)

    with colB:
        if st.button("Save to Leaderboard" if lang=="English" else "حفظ في لوحة الترتيب"):
            if classroom and player:
                save_score(classroom, player, st.session_state.competition_score)
                st.success("Saved!" if lang=="English" else "تم الحفظ!")

    # Show score
    st.metric("Your Score" if lang=="English" else "نقاطك", st.session_state.competition_score)

    # Live leaderboard
    if classroom:
        st.subheader("Live Leaderboard" if lang=="English" else "لوحة الترتيب")
        scores = get_scores(classroom)
        if scores:
            import pandas as pd
            df = pd.DataFrame(scores, columns=["Student", "Score"])
            df = df.sort_values("Score", ascending=False)
            st.table(df)

