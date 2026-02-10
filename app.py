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
# Qs = c + dP
# ---------------------------------
eq_price = (a - c) / (b + d)
eq_quantity = a - b * eq_price

# ---------------------------------
# Price slider (restricted range)
# ---------------------------------
price = st.slider(
    PRICE_LABEL,
    min_value=int(eq_price * 0.5),
    max_value=int(eq_price * 1.5),
    value=int(eq_price)
)

# ---------------------------------
# Quantities
# ---------------------------------
Qd_value = max(0, a - b * price)
Qs_value = max(0, c + d * price)

# ---------------------------------
# Market status
# ---------------------------------
if price < eq_price:
    market_status = SHORTAGE
elif price > eq_price:
    market_status = SURPLUS
else:
    market_status = EQUILIBRIUM

# ---------------------------------
# Results table
# ---------------------------------
results = pd.DataFrame({
    PRICE_LABEL: [round(price, 2)],
    QD: [round(Qd_value, 2)],
    QS: [round(Qs_value, 2)],
    STATUS: [market_status]
})

st.subheader(RESULTS)
st.table(results)

st.write(f"**{EQ_PRICE}: {round(eq_price,2)}**")

# ---------------------------------
# Graphical visualization
# ---------------------------------
price_range = np.linspace(eq_price * 0.5, eq_price * 1.5, 50)
demand_curve = a - b * price_range
supply_curve = c + d * price_range

graph_data = pd.DataFrame({
    "Demand": demand_curve,
    "Supply": supply_curve
}, index=price_range)

st.line_chart(graph_data)

# ---------------------------------
# Visual explanation
# ---------------------------------
if market_status == SHORTAGE:
    st.warning(
        "At this price, quantity demanded exceeds quantity supplied (Shortage)."
        if lang == "English"
        else
        "عند هذا السعر، الكمية المطلوبة أكبر من الكمية المعروضة (عجز)."
    )

elif market_status == SURPLUS:
    st.info(
        "At this price, quantity supplied exceeds quantity demanded (Surplus)."
        if lang == "English"
        else
        "عند هذا السعر، الكمية المعروضة أكبر من الكمية المطلوبة (فائض)."
    )

else:
    st.success(
        "Market equilibrium: quantity demanded equals quantity supplied."
        if lang == "English"
        else
        "توازن السوق: الكمية المطلوبة تساوي الكمية المعروضة."
    )

st.caption(
    "The shaded price range ensures that supply and demand always intersect."
    if lang == "English"
    else
    "تم تحديد مجال السعر بحيث يضمن تقاطع العرض والطلب دائماً."
)

# =================================
# MACROECONOMICS
# =================================
st.markdown("---")
st.header(MACRO)
st.info(COMING)

# ---------------------------------
# Close RTL container
# ---------------------------------
if lang == "العربية":
    st.markdown("</div>", unsafe_allow_html=True)
