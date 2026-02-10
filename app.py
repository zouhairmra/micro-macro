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
    EQ_PRICE = "سعر التوازن"

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
    EQ_PRICE = "Equilibrium Price"

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

# ---------------------------------
# Market parameters (fixed per run)
# ---------------------------------
a = np.random.randint(140, 180)   # Demand intercept
b = np.random.randint(1, 3)       # Demand slope
c = np.random.randint(10, 40)     # Supply intercept
d = np.random.randint(1, 3)       # Supply slope

# ---------------------------------
# Equilibrium calculation
# Qd = a - bP
#
