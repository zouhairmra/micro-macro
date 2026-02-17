import streamlit as st
from modules import supply_demand, elasticity, production_cost, quiz

st.set_page_config(page_title="منصة الاقتصاد الجزئي", layout="wide")

# RTL support
st.markdown("""
    <style>
    body {
        direction: RTL;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📘 منصة مبادئ الاقتصاد الجزئي التفاعلية")

st.sidebar.title("القائمة الرئيسية")

menu = st.sidebar.radio(
    "اختر الفصل",
    [
        "العرض والطلب",
        "المرونة",
        "دالة الإنتاج والتكاليف",
        "اختبار تفاعلي"
    ]
)

if menu == "العرض والطلب":
    supply_demand.run()

elif menu == "المرونة":
    elasticity.run()

elif menu == "دالة الإنتاج والتكاليف":
    production_cost.run()

elif menu == "اختبار تفاعلي":
    quiz.run()
