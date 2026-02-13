import streamlit as st
import time
import random

def generate_question():
    return {"question": "What is GDP?", "answer": "Gross Domestic Product"}

def run(lang="English"):
    st.header("Teacher Panel" if lang=="English" else "لوحة المعلم")
    password = st.text_input("Enter Teacher Password" if lang=="English" else "أدخل كلمة المرور", type="password")
    if password == "admin123":
        st.success("Teacher mode activated" if lang=="English" else "تم تفعيل وضع المعلم")
        duration = st.slider("Question duration (seconds)", 5, 60, 20)
        if st.button("Start Competition" if lang=="English" else "ابدأ المسابقة"):
            st.session_state.current_question = generate_question()
            st.session_state.question_start_time = time.time()
        if st.button("Stop Competition" if lang=="English" else "أوقف المسابقة"):
            st.session_state.current_question = None
        if st.session_state.current_question:
            st.write(st.session_state.current_question["question"])
    else:
        st.warning("Enter correct password" if lang=="English" else "أدخل كلمة المرور الصحيحة")
