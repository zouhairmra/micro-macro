import streamlit as st
import random
from config import get_text

def run(lang="English"):
    st.header(get_text("chatbot", lang))
    if "chatbot_score" not in st.session_state:
        st.session_state.chatbot_score = 0
    if "current_bot_question" not in st.session_state:
        st.session_state.current_bot_question = None
        st.session_state.current_bot_answer = None
        st.session_state.current_bot_options = None
        st.session_state.used_questions = []

    # Questions simples pour test
    questions_pool = [
        {"topic":"Basic Economy", "q":"What is opportunity cost?", "options":["Next best alternative foregone","Total cost","Sunk cost"], "answer":"Next best alternative foregone", "explanation":"Opportunity cost is the value of the next best alternative you give up."}
    ]

    if st.button("Ask the Bot for a Question" if lang=="English" else "اطلب سؤال من البوت"):
        available_questions = [q for q in questions_pool if q["q"] not in st.session_state.used_questions]
        if not available_questions:
            st.info("No more questions available!" if lang=="English" else "لا توجد أسئلة متاحة بعد!")
        else:
            question = random.choice(available_questions)
            st.session_state.current_bot_question = question["q"]
            st.session_state.current_bot_options = question["options"]
            st.session_state.current_bot_answer = question["answer"]
            st.session_state.used_questions.append(question["q"])

    if st.session_state.current_bot_question:
        st.subheader(st.session_state.current_bot_question)
        selected_answer = st.radio("Choose your answer:" if lang=="English" else "اختر إجابتك:", st.session_state.current_bot_options)
        if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
            if selected_answer == st.session_state.current_bot_answer:
                st.success("Correct!" if lang=="English" else "صحيح!")
                st.session_state.chatbot_score += 10
            else:
                st.error(f"Wrong! Correct answer: {st.session_state.current_bot_answer}" if lang=="English" else f"خطأ! الإجابة الصحيحة: {st.session_state.current_bot_answer}")
            st.session_state.current_bot_question = None
            st.session_state.current_bot_options = None
            st.session_state.current_bot_answer = None
    st.metric("Your Score" if lang=="English" else "نقاطك", st.session_state.chatbot_score)
