# -----------------------
# MICROECONOMICS
# -----------------------
st.header(MICRO)
st.write(
    "Supply and Demand Simulation"
    if lang == "English"
    else "محاكاة العرض والطلب"
)

price = st.slider(
    PRICE_LABEL,
    min_value=0,
    max_value=100,
    value=40
)

# Random market parameters
a = np.random.randint(120, 160)   # demand intercept
b = np.random.randint(1, 3)       # demand slope
c = np.random.randint(10, 40)     # supply intercept
d = np.random.randint(1, 3)       # supply slope

Qd = max(0, a - b * price)
Qs = max(0, c + d * price)

# Market outcome
if Qd > Qs:
    market_status = "Shortage" if lang == "English" else "عجز"
elif Qs > Qd:
    market_status = "Surplus" if lang == "English" else "فائض"
else:
    market_status = "Equilibrium" if lang == "English" else "توازن"

# Results table
results = pd.DataFrame({
    PRICE_LABEL: [price],
    "Quantity Demanded" if lang == "English" else "الكمية المطلوبة": [Qd],
    "Quantity Supplied" if lang == "English" else "الكمية المعروضة": [Qs],
    "Market Status" if lang == "English" else "حالة السوق": [market_status]
})

st.subheader("Results" if lang == "English" else "النتائج")
st.table(results)

# Supply & Demand graph
chart_data = pd.DataFrame({
    "Demand": [a, Qd],
    "Supply": [c, Qs]
})

st.line_chart(chart_data)

st.caption(
    "This simulation helps students visualize market equilibrium, shortages, and surpluses."
    if lang == "English"
    else
    "تساعد هذه المحاكاة الطلبة على فهم توازن السوق وحالات العجز والفائض."
)
