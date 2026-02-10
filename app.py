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
lang = st.sidebar.radio("Language / اللغة", ["English", "العربية"])

if lang == "العربية":
    st.markdown("<div dir='rtl'>", unsafe_allow_html=True)

    TITLE = "محاكاة الاقتصاد"
    MICRO = "الاقتصاد الجزئي"
    MACRO = "الاقتصاد الكلي"
    PRICE = "السعر"
    RESULTS = "النتائج"
    QD = "الكمية المطلوبة"
    QS = "الكمية المعروضة"
    STATUS = "حالة السوق"
    SHORTAGE = "عجز"
    SURPLUS = "فائض"
    EQUILIBRIUM = "توازن"
    EQ_PRICE = "سعر التوازن"
    DEMAND_SHIFT = "عوامل تحريك منحنى الطلب"
    SUPPLY_SHIFT = "عوامل تحريك منحنى العرض"
    ELASTICITY = "مرونة الطلب"
    COMING = "قريباً"

else:
    TITLE = "Economics Simulations"
    MICRO = "Microeconomics"
    MACRO = "Macroeconomics"
    PRICE = "Price"
    RESULTS = "Results"
    QD = "Quantity Demanded"
    QS = "Quantity Supplied"
    STATUS = "Market Status"
    SHORTAGE = "Shortage"
    SURPLUS = "Surplus"
    EQUILIBRIUM = "Equilibrium"
    EQ_PRICE = "Equilibrium Price"
    DEMAND_SHIFT = "Demand Curve Shifters"
    SUPPLY_SHIFT = "Supply Curve Shifters"
    ELASTICITY = "Elasticity of Demand"
    COMING = "Coming Soon"

# ---------------------------------
# Title
# ---------------------------------
st.title(TITLE)

# =================================
# MICROECONOMICS
# =================================
st.header(MICRO)

# =================================================
# 1️⃣ DEMAND & SUPPLY SHIFTERS
# =================================================
st.subheader(DEMAND_SHIFT)

demand_factor = st.selectbox(
    "Select a factor" if lang == "English" else "اختر عاملاً",
    ["None", "Income Increase", "Income Decrease", "Substitutes", "Population Growth"]
    if lang == "English"
    else
    ["لا شيء", "زيادة الدخل", "انخفاض الدخل", "سلع بديلة", "نمو السكان"]
)

st.subheader(SUPPLY_SHIFT)

supply_factor = st.selectbox(
    "Select a factor" if lang == "English" else "اختر عاملاً",
    ["None", "Technology Improvement", "Input Cost Increase", "Taxes"]
    if lang == "English"
    else
    ["لا شيء", "تحسن التكنولوجيا", "زيادة تكلفة المدخلات", "الضرائب"]
)

# Base parameters
a, b = 160, 2   # Demand
c, d = 20, 2    # Supply

# Apply demand shifts
if demand_factor in ["Income Increase", "زيادة الدخل", "Population Growth", "نمو السكان"]:
    a += 20
elif demand_factor in ["Income Decrease", "انخفاض الدخل"]:
    a -= 20

# Apply supply shifts
if supply_factor in ["Technology Improvement", "تحسن التكنولوجيا"]:
    c -= 10
elif supply_factor in ["Input Cost Increase", "زيادة تكلفة المدخلات", "Taxes", "الضرائب"]:
    c += 10

# =================================================
# 2️⃣ EQUILIBRIUM
# =================================================
st.subheader(EQUILIBRIUM)

eq_price = (a - c) / (b + d)
eq_quantity = a - b * eq_price

price = st.slider(
    PRICE,
    min_value=int(eq_price * 0.5),
    max_value=int(eq_price * 1.5),
    value=int(eq_price)
)

Qd_val = max(0, a - b * price)
Qs_val = max(0, c + d * price)

if price < eq_price:
    market_status = SHORTAGE
elif price > eq_price:
    market_status = SURPLUS
else:
    market_status = EQUILIBRIUM

results = pd.DataFrame({
    PRICE: [round(price, 2)],
    QD: [round(Qd_val, 2)],
    QS: [round(Qs_val, 2)],
    STATUS: [market_status]
})

st.write(f"**{EQ_PRICE}: {round(eq_price,2)}**")
st.table(results)

# Graph
price_range = np.linspace(eq_price * 0.5, eq_price * 1.5, 50)
demand_curve = a - b * price_range
supply_curve = c + d * price_range

graph_data = pd.DataFrame({
    "Demand": demand_curve,
    "Supply": supply_curve
}, index=price_range)

st.line_chart(graph_data)

# =================================================
# 3️⃣ ELASTICITY OF DEMAND (IMPROVED)
# =================================================
st.subheader(ELASTICITY)

st.write(
    "Price Elasticity of Demand (Midpoint Method)"
    if lang == "English"
    else
    "مرونة الطلب السعرية (طريقة المنتصف)"
)

# Two price points
P1 = st.slider(
    "Initial Price" if lang == "English" else "السعر الابتدائي",
    min_value=int(eq_price * 0.6),
    max_value=int(eq_price * 1.4),
    value=int(eq_price * 0.9)
)

P2 = st.slider

# =================================
# MACROECONOMICS
# =================================
st.markdown("---")
st.header(MACRO)
st.info(COMING)

# ---------------------------------
# Close RTL
# ---------------------------------
if lang == "العربية":
    st.markdown("</div>", unsafe_allow_html=True)
