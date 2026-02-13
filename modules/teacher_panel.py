import streamlit as st
import random
from utils import generate_question

def run(lang="English"):
    st.header("Teacher Control Panel" if lang=="English" else "لوحة التحكم للمعلم")

    password = st.text_input("Enter Teacher Password" if lang=="English" else "أدخل كلمة المرور", type="password")

    if password == "admin123":
        st.success("Teacher mode activated" if lang=="English" else "تم تفعيل وضع المعلم")

        # Question duration
        duration = st.slider(
            "Question duration (seconds)" if lang=="English" else "مدة السؤال (بالثواني)",
            5, 60, 20
        )
        st.session_state.question_duration = duration

        if st.button("Start Competition" if lang=="English" else "ابدأ المسابقة"):
            st.session_state.competition_active = True
            st.session_state.current_question = generate_question()
            st.session_state.question_start_time = time.time()

        if st.button("Stop Competition" if lang=="English" else "أوقف المسابقة"):
            st.session_state.competition_active = False

        if st.button("Next Question" if lang=="English" else "السؤال التالي"):
            st.session_state.current_question = generate_question()
            st.session_state.question_start_time = time.time()

        if st.session_state.get("current_question"):
            st.write(st.session_state.current_question["question"])
    else:
        if password:
            st.warning("Enter correct password" if lang=="English" else "أدخل كلمة المرور الصحيحة")
