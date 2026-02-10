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
# 3️⃣ ELASTICITY OF DEMAND (ADVANCED)
# =================================================
st.subheader(ELASTICITY)

st.write(
    "Elasticity along different demand curves and time horizons"
    if lang == "English"
    else
    "المرونة عبر منحنيات طلب مختلفة وعلى المدى القصير والطويل"
)

# ---------------------------------
# Demand curve type
# ---------------------------------
curve_type = st.selectbox(
    "Demand Curve Type" if lang == "English" else "نوع منحنى الطلب",
    ["Steep (Inelastic)", "Linear", "Flat (Elastic)"]
    if lang == "English"
    else
    ["حاد (غير مرن)", "خطي", "مسطح (مرن)"]
)

# Adjust slope based on curve type
if curve_type in ["Steep (Inelastic)", "حاد (غير مرن)"]:
    b_el = 4
elif curve_type in ["Flat (Elastic)", "مسطح (مرن)"]:
    b_el = 1
else:
    b_el = 2

# ---------------------------------
# Short run vs Long run
# ---------------------------------
time_horizon = st.radio(
    "Time Horizon" if lang == "English" else "الأفق الزمني",
    ["Short Run", "Long Run"]
    if lang == "English"
    else
    ["المدى القصير", "المدى الطويل"]
)

# Long run is more elastic
if time_horizon in ["Long Run", "المدى الطويل"]:
    b_el = b_el / 2

# ---------------------------------
# Business pricing decision
# ---------------------------------
st.markdown(
    "**Business Pricing Decision**"
    if lang == "English"
    else
    "**قرار التسعير للشركة**"
)

P1 = st.slider(
    "Initial Price" if lang == "English" else "السعر الابتدائي",
    min_value=int(eq_price * 0.6),
    max_value=int(eq_price * 1.4),
    value=int(eq_price * 0.9)
)

P2 = st.slider(
    "New Price" if lang == "English" else "السعر الجديد",
    min_value=int(eq_price * 0.6),
    max_value=int(eq_price * 1.4),
    value=int(eq_price * 1.1)
)

# ---------------------------------
# Quantities
# ---------------------------------
Q1 = max(0, a - b_el * P1)
Q2 = max(0, a - b_el * P2)

# ---------------------------------
# Midpoint elasticity
# ---------------------------------
elasticity = (
    ((Q2 - Q1) / ((Q1 + Q2) / 2)) /
    ((P2 - P1) / ((P1 + P2) / 2))
)

# ---------------------------------
# Total Revenue
# ---------------------------------
TR1 = P1 * Q1
TR2 = P2 * Q2

# ---------------------------------
# Elasticity classification
# ---------------------------------
if abs(elasticity) > 1:
    elasticity_type = "Elastic" if lang == "English" else "مرن"
elif abs(elasticity) < 1:
    elasticity_type = "Inelastic" if lang == "English" else "غير مرن"
else:
    elasticity_type = "Unit Elastic" if lang == "English" else "مرونة وحدية"

# ---------------------------------
# Results table
# ---------------------------------
elasticity_results = pd.DataFrame({
    PRICE: [round(P1, 2), round(P2, 2)],
    QD: [round(Q1, 2), round(Q2, 2)],
    "Total Revenue" if lang == "English" else "الإيراد الكلي": [round(TR1, 2), round(TR2, 2)]
}, index=[
    "Initial" if lang == "English" else "ابتدائي",
    "New" if lang == "English" else "جديد"
])

st.table(elasticity_results)

st.write(
    f"**Elasticity = {round(elasticity,2)} → {elasticity_type}**"
)

# ---------------------------------
# Managerial interpretation
# ---------------------------------
if abs(elasticity) > 1:
    st.success(
        "Demand is elastic. A price decrease increases total revenue."
        if lang == "English"
        else
        "الطلب مرن. تخفيض السعر يزيد الإيراد الكلي."
    )
else:
    st.info(
        "Demand is inelastic. A price increase increases total revenue."
        if lang == "English"
        else
        "الطلب غير مرن. رفع السعر يزيد الإيراد الكلي."
    )

# ---------------------------------
# Demand curve visualization
# ---------------------------------
price_range_el = np.linspace(P1 * 0.6, P2 * 1.4, 50)
demand_curve_el = a - b_el * price_range_el

elasticity_graph = pd.DataFrame({
    "Demand": demand_curve_el
}, index=price_range_el)

st.line_chart(elasticity_graph)

st.caption(
    "Elasticity differs across demand curves and increases in the long run."
    if lang == "English"
    else
    "تختلف المرونة باختلاف شكل منحنى الطلب وتزداد في المدى الطويل."
)

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
