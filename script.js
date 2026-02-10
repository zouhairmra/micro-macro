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
    market_status = "Sh_
