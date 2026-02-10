import streamlit as st
import numpy as np
import pandas as pd

# -----------------------
# Page config
# -----------------------
st.set_page_config(page_title="Economics Simulations", layout="centered")

# -----------------------
# Language toggle
# -----------------------
lang = st.sidebar.radio(
    "Language / اللغة",
    ["English", "العربية"]
)

if lang == "العربية":
    st.markdown("<div dir='rtl'>", unsafe_allow_html=True)
    TITLE = "محاكاة الاقتصاد"
    MICRO = "الاقتصاد الجزئي"
    MACRO = "الاقتصاد الكلي"
    PRICE_LABEL = "اختر السعر"
    RUN = "تشغيل المحاكاة"
    COMING = "قريباً"
    PROFIT = "الربح"
    QUANTITY = "الكمية"
else:
    TITLE = "Economics Simulations"
    MICRO = "Microeconomics"
    MACRO = "Macroeconomics"
    PRICE_LABEL = "Choose your price"
    RUN = "Run Simulation"
    COMING = "Coming Soon"
    PROFIT = "Profit"
    QUANTITY = "Quantity"

# -----------------------
# Title
# -----------------------
st.title(TITLE)

# -----------------------
# MICROECONOMICS
# -----------------------
st.header(MICRO)
st.write("Price Competition Simulation (Bertrand-style)")

price = st.number_input(PRICE_LABEL, min_value=0, value=30)

if st.button(RUN):
    mc = np.random.randint(10, 20)     # random marginal cost
    demand = 120
    quantity = max(0, demand - price)
    profit = (price - mc) * quantity

    results = pd.DataFrame({
        PRICE_LABEL: [price],
        QUANTITY: [quantity],
        PROFIT: [profit]
    })

    st.subheader("Results")
    st.table(results)

    # Demand curve (simple & academic)
    st.line_chart({
        "Demand": [120, quantity]
    })

    st.caption(
        "This simulation illustrates price competition and profit outcomes under random market conditions."
        if lang == "English"
        else
        "توضح هذه المحاكاة المنافسة السعرية وتأثيرها على الأرباح في ظل ظروف سوق عشوائية."
    )

# -----------------------
# MACROECONOMICS
# -----------------------
st.markdown("---")
st.header(MACRO)
st.info(COMING)

# Close RTL div
if lang == "العربية":
    st.markdown("</div>", unsafe_allow_html=True)
