import streamlit as st
import random

def run(lang="English"):
    st.header("Practice Quiz" if lang=="English" else "اختبار تدريبي")

    # Initialize score
    if "practice_score" not in st.session_state:
        st.session_state.practice_score = 0

    # Question bank
    questions = [
        {"q": "Elastic demand means elasticity is:", "options": [">1", "<1", "=1"], "answer": ">1"},
        {"q": "Inelastic demand means elasticity is:", "options": [">1", "<1", "=1"], "answer": "<1"},
        {"q": "Unit elastic demand means elasticity equals:", "options": [">1", "<1", "=1"], "answer": "=1"},
        {"q": "If price rises and total revenue rises, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"}
    ]

    # Select random question
    current_q = random.choice(questions)

    answer = st.radio(current_q["q"], current_q["options"])

    if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
        if answer == current_q["answer"]:
            st.success("Correct" if lang=="English" else "صحيح")
            st.session_state.practice_score += 1
        else:
            st.error("Incorrect" if lang=="English" else "خطأ")

    st.write("Score:" if lang=="English" else "النقاط", st.session_state.practice_score)
