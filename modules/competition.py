import streamlit as st
import random

# ==============================================
# Questions Pool
# ==============================================
questions_pool = [
    # Basic Economy
    {"topic":"Basic Economy", "q":"What is GDP?", "options":["Gross Domestic Product","Gross Domestic Profit","General Domestic Product"], "answer":"Gross Domestic Product","explanation":"GDP is the total value of goods and services produced in a country."},
    {"topic":"Basic Economy", "q":"What is opportunity cost?", "options":["Next best alternative foregone","Total cost","Sunk cost"], "answer":"Next best alternative foregone","explanation":"Opportunity cost is the value of the next best alternative you give up."},
    
    # Supply & Demand
    {"topic":"Supply & Demand", "q":"If demand increases, what happens to equilibrium price?", "options":["Increases","Decreases","Stays the same"], "answer":"Increases","explanation":"Higher demand pushes the equilibrium price up."},
    {"topic":"Supply & Demand", "q":"If supply decreases, what happens to equilibrium price?", "options":["Increases","Decreases","Stays the same"], "answer":"Increases","explanation":"Lower supply pushes price up."},
    
    # Elasticity
    {"topic":"Elasticity", "q":"Elastic demand has elasticity greater than?", "options":["1","0","-1"], "answer":"1","explanation":"Elastic demand: elasticity > 1."},
    {"topic":"Elasticity", "q":"Inelastic demand has elasticity less than?", "options":["1","0","-1"], "answer":"1","explanation":"Inelastic demand: elasticity < 1."},
    {"topic":"Elasticity", "q":"Unit elastic demand has elasticity equal to?", "options":["1","0","-1"], "answer":"1","explanation":"Unit elastic demand: elasticity = 1."},
    
    # Consumer Utility
    {"topic":"Consumer Utility", "q":"Law of diminishing marginal utility states?", "options":["Each additional unit gives less satisfaction","Each additional unit gives more satisfaction","Satisfaction remains constant"], "answer":"Each additional unit gives less satisfaction","explanation":"As you consume more, the extra satisfaction decreases."},
    {"topic":"Consumer Utility", "q":"Total utility is?", "options":["Sum of satisfaction from all units","Satisfaction from last unit","Average satisfaction"], "answer":"Sum of satisfaction from all units","explanation":"Total utility is the total satisfaction from all units consumed."}
]

# ==============================================
# Run Function
# ==============================================
def run(lang="English"):
    st.header("Live Classroom Competition" if lang=="English" else "مسابقة الصف المباشرة")
    
    # Initialize session state
    if "competition_score" not in st.session_state:
        st.session_state.competition_score = 0
    if "used_questions" not in st.session_state:
        st.session_state.used_questions = []
    if "current_question" not in st.session_state:
        st.session_state.current_question = None
    
    # ==========================================
    # Generate New Question
    # ==========================================
    if st.button("Next Question" if lang=="English" else "السؤال التالي"):
        available_questions = [q for q in questions_pool if q["q"] not in st.session_state.used_questions]
        if not available_questions:
            st.info("No more questions available!" if lang=="English" else "لا توجد أسئلة متاحة بعد!")
            return
        question = random.choice(available_questions)
        st.session_state.current_question = question
        st.session_state.used_questions.append(question["q"])
    
    # ==========================================
    # Display Current Question
    # ==========================================
    if st.session_state.current_question:
        q = st.session_state.current_question
        st.subheader(q["q"])
        selected_answer = st.radio("Choose your answer:" if lang=="English" else "اختر إجابتك:", q["options"])
        
        if st.button("Submit Answer" if lang=="English" else "إرسال الإجابة"):
            if selected_answer == q["answer"]:
                st.success("Correct!" if lang=="English" else "صحيح!")
                st.session_state.competition_score += 10
            else:
                st.error(f"Wrong! Correct answer: {q['answer']}" if lang=="English" else f"خطأ! الإجابة الصحيحة: {q['answer']}")
            st.info(q["explanation"] if lang=="English" else q["explanation"])
            st.session_state.current_question = None
    
    # ==========================================
    # Display Score
    # ==========================================
    st.metric("Your Score" if lang=="English" else "نقاطك", st.session_state.competition_score)
    
    # ==========================================
    # Reset Competition
    # ==========================================
    if st.button("Reset Competition" if lang=="English" else "إعادة تعيين المسابقة"):
        st.session_state.used_questions = []
        st.session_state.current_question = None
        st.session_state.competition_score = 0
