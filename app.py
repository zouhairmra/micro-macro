import streamlit as st
import numpy as np
import pandas as pd

# ---------------------------------
# Page configuration
# ---------------------------------
st.set_page_config(
    page_title="Economics Simulations",
    layout="centered"
)

# ---------------------------------
# Language toggle
# ---------------------------------
lang = st.sidebar.radio(
    "Language / اللغة",
    ["English", "العربية"]
)

if lang == "العربية":
    st.markdown("<div dir='rtl'>", unsafe_allow_html=True)

    TITLE = "محاكاة الاقتصاد"
    MICRO = "الاقتصاد الجزئي"
    MACRO = "الاقتصاد الكلي"
    PRICE_LABEL = "السعر"
    RESULTS = "النتائج"
    QD = "الكمية المطلوبة"
    QS = "الكمية المعروضة"
    STATUS = "حالة السوق"
    SHORTAGE = "عجز"
    SURPLUS = "فائض"
    EQUILIBRIUM = "توازن"
    COMING = "قريباً"

else:
    TITLE = "Economics Simulations"
    MICRO = "Microeconomics"
    MACRO = "Macroeconomics"
    PRICE_LABEL = "Price"
    RESULTS = "Results"
    QD = "Quantity Demanded"
    QS = "Quantity Supplied"
    STATUS = "Market Status"
    SHORTAGE = "Shortage"
    SURPLUS = "Surplus"
    EQUILIBRIUM = "Equilibrium"
    COMING = "Coming Soon"

# ---------------------------------
# Title
# ---------------------------------
st.title(TITLE)

# =================================
# MICROECONOMICS
# =================================
st.header(MICRO)

st.write(
    "Supply and Demand Simulation"
    if lang == "English"
    else
    "محاكاة العرض والطلب"
)

# Price selection
price = st.slider(
    PRICE_LABEL,
    min_value=0,
    max_value=100,
    value=40
)

# Random market parameters
a = np.random.randint(120, 160)   # Demand intercept
b = np.random.randint(1, 3)       # Demand slope
c = np.random.randint(10, 40)     # Supply intercept
d = np.random.randint(1, 3)       # Supply slope

# Quantities
Qd_value = max(0, a - b * price)
