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
    else "المرونة عبر منحنيات طلب مختلفة وعلى المدى القصير والطويل"
)

# ---------------------------------
# Demand curve type
# ---------------------------------
curve_type = st.selectbox(
    "Demand Curve Type" if lang == "English" else "نوع منحنى الطلب",
    ["Steep (Inelastic)", "Linear", "Flat (Elastic)"]
    if lang == "English"
    else ["حاد (غير مرن)", "خطي", "مسطح (مرن)"]
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
    else ["المدى القصير", "المدى الطويل"]
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
    else "**قرار التسعير للشركة**"
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
        else "الطلب مرن. تخفيض السعر يزيد الإيراد الكلي."
    )
else:
    st.info(
        "Demand is inelastic. A price increase increases total revenue."
        if lang == "English"
        else "الطلب غير مرن. رفع السعر يزيد الإيراد الكلي."
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
    else "تختلف المرونة باختلاف شكل منحنى الطلب وتزداد في المدى الطويل."
)

# =================================================
# 4️⃣ CROSS-PRICE ELASTICITY
# =================================================
st.subheader(
    "Cross-Price Elasticity" if lang == "English" else "المرونة العرضية"
)

st.markdown(
    "Effect of a change in the price of a related good (X) on quantity demanded of this good."
    if lang == "English"
    else "تأثير تغير سعر سلعة مرتبطة (X) على الكمية المطلوبة من هذه السلعة."
)

Px1 = st.slider(
    "Initial Price of Related Good X" if lang == "English" else "السعر الابتدائي للسلعة X",
    min_value=int(eq_price * 0.5),
    max_value=int(eq_price * 1.5),
    value=int(eq_price * 0.9)
)

Px2 = st.slider(
    "New Price of Related Good X" if lang == "English" else "السعر الجديد للسلعة X",
    min_value=int(eq_price * 0.5),
    max_value=int(eq_price * 1.5),
    value=int(eq_price * 1.1)
)

# Cross-effect parameter (positive = substitutes, negative = complements)
cross_effect = st.slider(
    "Cross Effect Strength"
    if lang == "English"
    else "قوة العلاقة بين السلعتين",
    min_value=-2.0,
    max_value=2.0,
    value=1.0,
    step=0.1
)

Qx1 = max(0, a - b_el * P1 + cross_effect * Px1)
Qx2 = max(0, a - b_el * P1 + cross_effect * Px2)

cross_elasticity = (
    ((Qx2 - Qx1) / ((Qx1 + Qx2) / 2)) /
    ((Px2 - Px1) / ((Px1 + Px2) / 2))
)

if cross_elasticity > 0:
    cross_type = "Substitutes" if lang == "English" else "سلع بديلة"
elif cross_elasticity < 0:
    cross_type = "Complements" if lang == "English" else "سلع تكميلية"
else:
    cross_type = "Independent Goods" if lang == "English" else "سلع مستقلة"

st.write(
    f"**Cross-Price Elasticity = {round(cross_elasticity,2)} → {cross_type}**"
)

# ----- GRAPH -----
px_range = np.linspace(Px1 * 0.6, Px2 * 1.4, 50)
cross_curve = a - b_el * P1 + cross_effect * px_range

cross_graph = pd.DataFrame({
    "Quantity Demanded": cross_curve
}, index=px_range)

st.line_chart(cross_graph)

st.caption(
    "Positive elasticity → Substitutes | Negative elasticity → Complements"
    if lang == "English"
    else "إشارة موجبة → بدائل | إشارة سالبة → مكملات"
)
# =================================================
# 5️⃣ INCOME ELASTICITY
# =================================================
st.subheader(
    "Income Elasticity" if lang == "English" else "مرونة الدخل"
)

st.markdown(
    "Effect of income changes on quantity demanded."
    if lang == "English"
    else "تأثير تغير الدخل على الكمية المطلوبة."
)

Y1 = st.slider(
    "Initial Income" if lang == "English" else "الدخل الابتدائي",
    min_value=1000,
    max_value=20000,
    value=5000,
    step=500
)

Y2 = st.slider(
    "New Income" if lang == "English" else "الدخل الجديد",
    min_value=1000,
    max_value=20000,
    value=8000,
    step=500
)

income_effect = st.slider(
    "Income Effect Strength"
    if lang == "English"
    else "قوة تأثير الدخل",
    min_value=-0.005,
    max_value=0.005,
    value=0.002,
    step=0.0005
)

Qi1 = max(0, a - b_el * P1 + income_effect * Y1)
Qi2 = max(0, a - b_el * P1 + income_effect * Y2)

income_elasticity = (
    ((Qi2 - Qi1) / ((Qi1 + Qi2) / 2)) /
    ((Y2 - Y1) / ((Y1 + Y2) / 2))
)

if income_elasticity > 1:
    income_type = "Luxury Good" if lang == "English" else "سلعة كمالية"
elif income_elasticity > 0:
    income_type = "Normal Good" if lang == "English" else "سلعة عادية"
elif income_elasticity < 0:
    income_type = "Inferior Good" if lang == "English" else "سلعة دنيا"
else:
    income_type = "Income Neutral" if lang == "English" else "محايدة للدخل"

st.write(
    f"**Income Elasticity = {round(income_elasticity,2)} → {income_type}**"
)

# ----- GRAPH -----
income_range = np.linspace(Y1 * 0.6, Y2 * 1.4, 50)
income_curve = a - b_el * P1 + income_effect * income_range

income_graph = pd.DataFrame({
    "Quantity Demanded": income_curve
}, index=income_range)

st.line_chart(income_graph)

st.caption(
    "Positive → Normal/Luxury | Negative → Inferior"
    if lang == "English"
    else "موجب → عادية/كمالية | سالب → دنيا"
)
# =================================================
# 6️⃣ AUTO-GENERATED QUIZ
# =================================================
st.subheader(
    "Elasticity Quiz"
    if lang == "English"
    else "اختبار المرونة"
)

# Initialize score
if "score" not in st.session_state:
    st.session_state.score = 0

if "question_number" not in st.session_state:
    st.session_state.question_number = 1

st.markdown(
    f"**Question {st.session_state.question_number}**"
    if lang == "English"
    else f"**السؤال {st.session_state.question_number}**"
)

# Randomly choose question type
import random
question_type = random.choice(["own", "cross", "income"])

# -------------------------------
# OWN-PRICE QUESTION
# -------------------------------
if question_type == "own":
    
    correct_answer = elasticity_type
    
    question_text = (
        f"If price changes from {P1} to {P2}, demand is:"
        if lang == "English"
        else f"إذا تغير السعر من {P1} إلى {P2} فإن الطلب:"
    )
    
    options = ["Elastic", "Inelastic", "Unit Elastic"] if lang == "English" else ["مرن", "غير مرن", "مرونة وحدية"]

# -------------------------------
# CROSS-PRICE QUESTION
# -------------------------------
elif question_type == "cross":
    
    correct_answer = cross_type
    
    question_text = (
        "The relationship between the two goods is:"
        if lang == "English"
        else "العلاقة بين السلعتين هي:"
    )
    
    options = ["Substitutes", "Complements", "Independent Goods"] if lang == "English" else ["سلع بديلة", "سلع تكميلية", "سلع مستقلة"]

# -------------------------------
# INCOME QUESTION
# -------------------------------
else:
    
    correct_answer = income_type
    
    question_text = (
        "Based on income elasticity, the good is:"
        if lang == "English"
        else "بناءً على مرونة الدخل، السلعة هي:"
    )
    
    options = ["Luxury Good", "Normal Good", "Inferior Good", "Income Neutral"] if lang == "English" else ["سلعة كمالية", "سلعة عادية", "سلعة دنيا", "محايدة للدخل"]

st.write(question_text)

answer = st.radio(
    "Choose your answer:" if lang == "English" else "اختر الإجابة:",
    options
)

if st.button("Submit Answer" if lang == "English" else "إرسال الإجابة"):
    
    if answer == correct_answer:
        st.success("Correct!" if lang == "English" else "إجابة صحيحة!")
        st.session_state.score += 1
    else:
        st.error(
            f"Wrong! Correct answer: {correct_answer}"
            if lang == "English"
            else f"إجابة خاطئة! الإجابة الصحيحة: {correct_answer}"
        )
    
    st.session_state.question_number += 1

st.write(
    f"Score: {st.session_state.score}"
    if lang == "English"
    else f"النتيجة: {st.session_state.score}"
)
# =================================================
# 7️⃣ CLASSROOM COMPETITION MODE
# =================================================
st.subheader(
    "Classroom Competition"
    if lang == "English"
    else "مسابقة الصف"
)

player_name = st.text_input(
    "Enter your name" if lang == "English" else "أدخل اسمك"
)

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = {}

if st.button("Save Score" if lang == "English" else "حفظ النتيجة"):
    
    if player_name:
        st.session_state.leaderboard[player_name] = st.session_state.score
        st.success(
            "Score saved!"
            if lang == "English"
            else "تم حفظ النتيجة!"
        )

# Display leaderboard
if st.session_state.leaderboard:
    
    leaderboard_df = pd.DataFrame(
        list(st.session_state.leaderboard.items()),
        columns=[
            "Player" if lang == "English" else "الطالب",
            "Score" if lang == "English" else "النتيجة"
        ]
    ).sort_values(
        by="Score" if lang == "English" else "النتيجة",
        ascending=False
    )
    
    st.table(leaderboard_df)

if st.button("Reset Competition" if lang == "English" else "إعادة تعيين المسابقة"):
    st.session_state.leaderboard = {}
    st.session_state.score = 0
    st.session_state.question_number = 1

