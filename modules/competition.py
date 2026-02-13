import streamlit as st
import random
from database import save_score, get_scores

def run(lang="English"):
    st.header("Live Classroom Competition" if lang=="English" else "مسابقة الصف المباشرة")

    # -----------------------------
    # Student Info
    # -----------------------------
    col1, col2 = st.columns(2)
    with col1:
        classroom = st.text_input("Classroom Code" if lang=="English" else "رمز الصف")
        player = st.text_input("Student Name" if lang=="English" else "اسم الطالب")

    # Initialize session state variables
    if "competition_score" not in st.session_state:
        st.session_state.competition_score = 0
    if "question_id" not in st.session_state:
        st.session_state.question_id = 1
    if "questions_asked" not in st.session_state:
        st.session_state.questions_asked = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = None

    # -----------------------------
    # Full Question Bank
    # -----------------------------
    questions = [
        # Basic Economy
        {"topic":"Basic", "q": "What is opportunity cost?", "options": ["Next best alternative foregone", "Total cost", "Sunk cost"], "answer": "Next best alternative foregone"},
        {"topic":"Basic", "q": "Law of demand states:", "options": ["Price ↑ → Quantity ↓", "Price ↑ → Quantity ↑", "Price ↓ → Quantity ↓"], "answer": "Price ↑ → Quantity ↓"},
        # Supply & Demand
        {"topic":"Supply & Demand", "q": "An increase in supply with demand constant causes price to:", "options": ["Rise", "Fall", "Remain same"], "answer": "Fall"},
        {"topic":"Supply & Demand", "q": "A shortage occurs when:", "options": ["Demand > Supply", "Supply > Demand", "Demand = Supply"], "answer": "Demand > Supply"},
        {"topic":"Supply & Demand", "q": "A surplus occurs when:", "options": ["Demand > Supply", "Supply > Demand", "Demand = Supply"], "answer": "Supply > Demand"},
        # Elasticity
        {"topic":"Elasticity", "q": "If elasticity > 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Elastic"},
        {"topic":"Elasticity", "q": "If elasticity < 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"},
        {"topic":"Elasticity", "q": "If elasticity = 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Unit Elastic"},
        {"topic":"Elasticity", "q": "Unit elastic demand means:", "options": ["TR unchanged", "TR rises", "TR falls"], "answer": "TR unchanged"},
        # Consumer Utility
        {"topic":"Consumer Utility", "q": "Marginal utility measures:", "options": ["Utility from one more unit", "Total utility", "Total revenue"], "answer": "Utility from one more unit"},
        {"topic":"Consumer Utility", "q": "Law of diminishing marginal utility states:", "options": ["MU decreases as consumption increases", "MU increases as consumption increases", "MU remains constant"], "answer": "MU decreases as consumption increases"},
        {"topic":"Consumer Utility", "q": "Total utility is:", "options": ["Sum of utilities of all units consumed", "Utility of last unit", "Price x Quantity"], "answer": "Sum of utilities of all units consumed"},
    ]

    # -----------------------------
    # Select Next Question
    # -----------------------------
    def get_next_question():
        remaining = [q for q in questions if q not in st.session_state.questions_asked]
        if remaining:
            question = random.choice(remaining)
            st.session_state.questions_asked.append(question)
            return question
        else:
            # Reset after all questions used
            st.session_state.questions_asked = []
            return random.choice(questions)

    if st.session_state.current_question is None:
        st.session_state.current_question = get_next_question()

    q = st.session_state.current_question
    st.subheader(f"Question {st.session_state.question_id} ({q['topic']})" if lang=="English" else f"السؤال {st.session_state.question_id} ({q['topic']})")
    answer = st.radio(q["q"], q["options"])

    # -----------------------------
    # Submit Answer
    # -----------------------------
    if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
        if answer == q["answer"]:
            st.success("Correct!" if lang=="English" else "صحيح!")
            st.session_state.competition_score += 10
        else:
            st.error(f"Wrong! Correct answer: {q['answer']}" if lang=="English" else f"خطأ! الإجابة الصحيحة: {q['answer']}")

    # -----------------------------
    # Next Question Button
    # -----------------------------
    if st.button("Next Question" if lang=="English" else "السؤال التالي"):
        st.session_state.current_question = get_next_question()
        st.session_state.question_id += 1

    # -----------------------------
    # Save Score
    # -----------------------------
    if st.button("Save to Leaderboard" if lang=="English" else "حفظ في لوحة الترتيب"):
        if classroom and player:
            save_score(classroom, player, st.session_state.competition_score)
            st.success("Saved!" if lang=="English" else "تم الحفظ!")

    # -----------------------------
    # Show Score
    # -----------------------------
    st.metric("Your Score" if lang=="English" else "نقاطك", st.session_state.competition_score)

    # -----------------------------
    # Live Leaderboard
    # -----------------------------
    if classroom:
        st.subheader("Live Leaderboard" if lang=="English" else "لوحة الترتيب")
        scores = get_scores(classroom)
        if scores:
            import pandas as pd
            df = pd.DataFrame(scores, columns=["Student", "Score"])
            df = df.sort_values("Score", ascending=False)
            st.table(df)

    # -----------------------------
    # Reset Competition
    # -----------------------------
    if st.button("Reset Competition" if lang=="English" else "إعادة تعيين المسابقة"):
        st.session_state.competition_score = 0
        st.session_state.question_id = 1
        st.session_state.current_question = None
        st.session_state.questions_asked = []
        st.success("Competition Reset" if lang=="English" else "تم إعادة تعيين المسابقة")
