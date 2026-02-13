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

    with col2:
        if "competition_score" not in st.session_state:
            st.session_state.competition_score = 0
        if "question_id" not in st.session_state:
            st.session_state.question_id = 1

    # -----------------------------
    # Question Bank
    # -----------------------------
    questions = [
        # Elasticity
        {"q": "If elasticity > 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Elastic"},
        {"q": "If elasticity < 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"},
        {"q": "If elasticity = 1, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Unit Elastic"},
        # Demand & Supply
        {"q": "If price rises and total revenue rises, demand is:", "options": ["Elastic", "Inelastic", "Unit Elastic"], "answer": "Inelastic"},
        {"q": "An increase in supply with demand constant causes price to:", "options": ["Rise", "Fall", "Remain same"], "answer": "Fall"},
        {"q": "A shortage occurs when:", "options": ["Demand > Supply", "Supply > Demand", "Demand = Supply"], "answer": "Demand > Supply"},
        {"q": "A surplus occurs when:", "options": ["Demand > Supply", "Supply > Demand", "Demand = Supply"], "answer": "Supply > Demand"},
        {"q": "Unit elastic demand means:", "options": ["TR unchanged", "TR rises", "TR falls"], "answer": "TR unchanged"},
        # Microeconomics
        {"q": "Opportunity cost is:", "options": ["Next best alternative foregone", "Total cost", "Sunk cost"], "answer": "Next best alternative foregone"},
        {"q": "Marginal cost is:", "options": ["Cost of producing one more unit", "Average cost", "Total cost"], "answer": "Cost of producing one more unit"},
        {"q": "A perfectly competitive firm is a price:", "options": ["Taker", "Maker", "Setter"], "answer": "Taker"},
        {"q": "Law of demand states:", "options": ["Price ↑ → Quantity ↓", "Price ↑ → Quantity ↑", "Price ↓ → Quantity ↓"], "answer": "Price ↑ → Quantity ↓"}
    ]

    # -----------------------------
    # Select or Reset Current Question
    # -----------------------------
    if "current_question" not in st.session_state or st.session_state.current_question is None:
        st.session_state.current_question = random.choice(questions)

    q = st.session_state.current_question
    st.subheader(f"Question {st.session_state.question_id}")

    # Show question options
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
        st.session_state.question_id += 1
        st.session_state.current_question = random.choice(questions)

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
        st.session_state.leaderboard = {}
        st.success("Competition Reset" if lang=="English" else "تم إعادة تعيين المسابقة")
