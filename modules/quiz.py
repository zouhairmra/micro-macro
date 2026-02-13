import streamlit as st
import random

def run(lang="English"):
    st.header("Practice Quiz" if lang=="English" else "الاختبار التدريبي")
    if "practice_score" not in st.session_state:
        st.session_state.practice_score = 0

    questions = [
        ("Elastic demand means elasticity is:", ">1"),
        ("Inelastic demand means elasticity is:", "<1"),
        ("Unit elastic demand means elasticity equals:", "=1")
    ] if lang=="English" else [
        ("الطلب المرن يعني أن المرونة تساوي:", ">1"),
        ("الطلب غير المرن يعني أن المرونة تساوي:", "<1"),
        ("الطلب ذو المرونة الوحدة يعني أن المرونة تساوي:", "=1")
    ]

    q = random.choice(questions)
    answer = st.radio(q[0], [">1","<1","=1"])
    if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
        if answer == q[1]:
            st.success("Correct" if lang=="English" else "صحيح")
            st.session_state.practice_score += 1
        else:
            st.error("Incorrect" if lang=="English" else "خطأ")
    st.write("Score:", st.session_state.practice_score)
