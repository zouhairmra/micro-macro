import streamlit as st
import random
import time
from config import get_text

def run(lang="English"):
    st.header(get_text("competition", lang))  # Titre du module

    # =============================
    # Initialisation session state
    # =============================
    if "competition_score" not in st.session_state:
        st.session_state.competition_score = 0
    if "competition_question_id" not in st.session_state:
        st.session_state.competition_question_id = 1
    if "competition_current_question" not in st.session_state:
        st.session_state.competition_current_question = None
        st.session_state.competition_used_questions = []

    # =============================
    # Questions avec explications
    # =============================
    questions_pool = [
        # Basic Economy
        {"topic":"Basic Economy", "q":"What is opportunity cost?", "options":["Next best alternative foregone","Total cost","Sunk cost"], "answer":"Next best alternative foregone", "explanation":"Opportunity cost is the value of the next best alternative you give up."},
        # Supply & Demand
        {"topic":"Supply & Demand", "q":"If supply increases and demand stays the same, what happens to price?", "options":["Price falls","Price rises","Price unchanged"], "answer":"Price falls", "explanation":"When supply increases, the market has more goods, leading to a lower price if demand is constant."},
        # Elasticity
        {"topic":"Elasticity", "q":"If demand is inelastic, what happens to total revenue when price rises?", "options":["Total revenue rises","Total revenue falls","Total revenue unchanged"], "answer":"Total revenue rises", "explanation":"With inelastic demand, quantity demanded changes little, so raising price increases revenue."},
        # Consumer Utility
        {"topic":"Consumer Utility", "q":"Law of diminishing marginal utility states that:", "options":["MU decreases as consumption increases","MU increases","MU constant"], "answer":"MU decreases as consumption increases", "explanation":"As a person consumes more units of a good, the additional satisfaction from each unit declines."},
    ]

    # Version arabe si nécessaire
    if lang != "English":
        questions_pool = [
            {"topic":"الاقتصاد الأساسي", "q":"ما هو تكلفة الفرصة عند اختيار بديل على آخر؟", "options":["أفضل بديل متروك","التكلفة الكلية","التكلفة الغارقة"], "answer":"أفضل بديل متروك", "explanation":"تكلفة الفرصة هي قيمة البديل الأفضل التالي الذي تتخلى عنه."},
            {"topic":"العرض والطلب", "q":"إذا زاد العرض وبقي الطلب ثابتًا، ماذا يحدث للسعر؟", "options":["السعر ينخفض","السعر يرتفع","السعر يبقى ثابتًا"], "answer":"السعر ينخفض", "explanation":"عندما يزيد العرض ويظل الطلب ثابتًا، يكون هناك فائض يؤدي إلى انخفاض السعر."},
            {"topic":"المرونة", "q":"إذا كان الطلب غير مرن، ماذا يحدث للإيرادات الكلية عندما يرتفع السعر؟", "options":["الإيرادات الكلية ترتفع","الإيرادات الكلية تنخفض","الإيرادات الكلية تبقى ثابتة"], "answer":"الإيرادات الكلية ترتفع", "explanation":"عندما يكون الطلب غير مرن، فإن الكمية المطلوبة تتغير قليلًا، لذا زيادة السعر تزيد الإيرادات."},
            {"topic":"منفعة المستهلك", "q":"ينص قانون المنفعة الحدية المتناقصة على أن:", "options"
