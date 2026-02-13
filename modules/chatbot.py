import streamlit as st
import random

def run(lang="English"):
    st.header("AI Question Bot" if lang=="English" else "بوت الأسئلة الذكي")

    # Initialize session state
    if "chatbot_score" not in st.session_state:
        st.session_state.chatbot_score = 0
    if "current_bot_question" not in st.session_state:
        st.session_state.current_bot_question = None
        st.session_state.current_bot_answer = None
        st.session_state.current_bot_options = None

    # Define question templates
    questions_pool = [
        {"topic":"Basic Economy", "q":"What is opportunity cost?", "options":["Next best alternative foregone","Total cost","Sunk cost"], "answer":"Next best alternative foregone"},
        {"topic":"Supply & Demand", "q":"If supply increases and demand stays the same, what happens to price?", "options":["Price falls","Price rises","Price unchanged"], "answer":"Price falls"},
        {"topic":"Elasticity", "q":"If demand is inelastic, what happens to total revenue when price rises?", "options":["Total revenue rises","Total revenue falls","Total revenue unchanged"], "answer":"Total revenue falls"},
        {"topic":"Consumer Utility", "q":"Law of diminishing marginal utility states that:", "options":["MU decreases as consumption increases","MU increases","MU constant"], "answer":"MU decreases as consumption increases"}
    ]

    arabic_pool = [
        {"topic":"الاقتصاد الأساسي", "q":"ما هو تكلفة الفرصة عند اختيار بديل على آخر؟", "options":["أفضل بديل متروك","التكلفة الكلية","التكلفة الغارقة"], "answer":"أفضل بديل متروك"},
        {"topic":"العرض والطلب", "q":"إذا زاد العرض وبقي الطلب ثابتًا، ماذا يحدث للسعر؟", "options":["السعر ينخفض","السعر يرتفع","السعر يبقى ثابتًا"], "answer":"السعر ينخفض"},
        {"topic":"المرونة", "q":"إذا كان الطلب غير مرن، ماذا يحدث للإيرادات الكلية عندما يرتفع السعر؟", "options":["الإيرادات الكلية ترتفع","الإيرادات الكلية تنخفض","الإيرادات الكلية تبقى ثابتة"], "answer":"الإيرادات الكلية تنخفض"},
        {"topic":"منفعة المستهلك", "q":"ينص قانون المنفعة الحدية المتناقصة على أن:", "options":["المنفعة الحدية تنخفض مع زيادة الاستهلاك","المنفعة الحدية ترتفع","المنفعة الحدية تبقى ثابتة"], "answer":"المنفعة الحدية تنخفض مع زيادة الاستهلاك"}
    ]

    pool = questions_pool if lang=="English" else arabic_pool

    # Ask Bot Button
    if st.button("Ask the Bot for a Question" if lang=="English" else "اطلب سؤال من البوت"):
        question = random.choice(pool)
        st.session_state.current_bot_question = question["q"]
        st.session_state.current_bot_options = question["options"]
        st.session_state.current_bot_answer = question["answer"]

    # Display Question
    if st.session_state.current_bot_question:
        st.subheader(f"Topic: {pool[0]['topic']}" if lang=="English" else f"الموضوع: {pool[0]['topic']}")
        selected_answer = st.radio("Choose your answer:" if lang=="English" else "اختر إجابتك:", st.session_state.current_bot_options)

        # Submit Answer
        if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
            if selected_answer == st.session_state.current_bot_answer:
                st.success("Correct!" if lang=="English" else "صحيح!")
                st.session_state.chatbot_score += 10
            else:
                st.error(f"Wrong! Correct answer: {st.session_state.current_bot_answer}" if lang=="English" else f"خطأ! الإجابة الصحيحة: {st.session_state.current_bot_answer}")
            
            # Reset current question for next round
            st.session_state.current_bot_question = None
            st.session_state.current_bot_options = None
            st.session_state.current_bot_answer = None

    # Display Score
    st.metric("Your Score" if lang=="English" else "نقاطك", st.session_state.chatbot_score)
