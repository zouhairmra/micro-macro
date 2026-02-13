import streamlit as st
import random

def run(lang="English"):
    st.header("AI Question Bot" if lang=="English" else "بوت الأسئلة الذكي")

    topics = ["Basic Economy", "Supply & Demand", "Elasticity", "Consumer Utility"]
    arabic_topics = ["الاقتصاد الأساسي", "العرض والطلب", "المرونة", "منفعة المستهلك"]

    if "chatbot_score" not in st.session_state:
        st.session_state.chatbot_score = 0

    if "current_bot_question" not in st.session_state:
        st.session_state.current_bot_question = None
        st.session_state.current_bot_answer = None

    # -----------------------------
    # Generate Question
    # -----------------------------
    if st.button("Ask the Bot for a Question" if lang=="English" else "اطلب سؤال من البوت"):
        topic_index = random.randint(0, 3)
        topic = topics[topic_index] if lang=="English" else arabic_topics[topic_index]

        # Simple AI-like generation using templates
        if topic_index == 0:  # Basic Economy
            question = "What is the opportunity cost of choosing one alternative over another?" if lang=="English" else "ما هو تكلفة الفرصة عند اختيار بديل على آخر؟"
            options = ["Next best alternative foregone", "Total cost", "Sunk cost"] if lang=="English" else ["أفضل بديل متروك", "التكلفة الكلية", "التكلفة الغارقة"]
            answer = options[0]
        elif topic_index == 1:  # Supply & Demand
            question = "If supply increases and demand stays the same, what happens to price?" if lang=="English" else "إذا زاد العرض وبقي الطلب ثابتًا، ماذا يحدث للسعر؟"
            options = ["Price falls", "Price rises", "Price unchanged"] if lang=="English" else ["السعر ينخفض", "السعر يرتفع", "السعر يبقى ثابتًا"]
            answer = options[0]
        elif topic_index == 2:  # Elasticity
            question = "If demand is inelastic, what happens to total revenue when price increases?" if lang=="English" else "إذا كان الطلب غير مرن، ماذا يحدث للإيرادات الكلية عندما يرتفع السعر؟"
            options = ["Total revenue rises", "Total revenue falls", "Total revenue unchanged"] if lang=="English" else ["الإيرادات الكلية ترتفع", "الإيرادات الكلية تنخفض", "الإيرادات الكلية تبقى ثابتة"]
            answer = options[0]
        elif topic_index == 3:  # Consumer Utility
            question = "Law of diminishing marginal utility states that:" if lang=="English" else "ينص قانون المنفعة الحدية المتناقصة على أن:"
            options = ["MU decreases as consumption increases", "MU increases as consumption increases", "MU remains constant"] if lang=="English" else ["المنفعة الحدية تنخفض مع زيادة الاستهلاك", "المنفعة الحدية ترتفع مع زيادة الاستهلاك", "المنفعة الحدية تبقى ثابتة"]
            answer = options[0]

        # Save in session
        st.session_state.current_bot_question = question
        st.session_state.current_bot_answer = answer
        st.session_state.current_bot_options = options

    # -----------------------------
    # Display Question
    # -----------------------------
    if st.session_state.current_bot_question:
        st.subheader(st.session_state.current_bot_question)
        selected = st.radio("Choose your answer:" if lang=="English" else "اختر إجابتك:", st.session_state.current_bot_options)

        if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
            if selected == st.session_state.current_bot_answer:
                st.success("Correct!" if lang=="English" else "صحيح!")
                st.session_state.chatbot_score += 10
            else:
                st.error(f"Wrong! Correct answer: {st.session_state.current_bot_answer}" if lang=="English" else f"خطأ! الإجابة الصحيحة: {st.session_state.current_bot_answer}")
