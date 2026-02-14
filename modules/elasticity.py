import streamlit as st


def run(lang="English"):

    # =========================
    # LANGUAGE
    # =========================

    if lang == "English":

        TITLE = "Elasticity Simulator (Law of Demand Consistent)"
        METHODS = [
            "Standard Price Elasticity",
            "Midpoint Elasticity",
            "Income Elasticity",
            "Cross-Price Elasticity"
        ]

        PRICE1 = "Initial Price"
        PRICE2 = "New Price"

        INCOME1 = "Initial Income"
        INCOME2 = "New Income"

        RESULT = "Elasticity"
        INTERPRET = "Interpretation"

        ELASTIC = "Elastic"
        INELASTIC = "Inelastic"
        UNIT = "Unit Elastic"

        NORMAL = "Normal good"
        INFERIOR = "Inferior good"

        SUBSTITUTE = "Substitute goods"
        COMPLEMENT = "Complement goods"

    else:

        TITLE = "محاكي المرونة (متوافق مع قانون الطلب)"
        METHODS = [
            "المرونة السعرية (الطريقة البسيطة)",
            "المرونة السعرية (طريقة نقطة الوسط)",
            "مرونة الدخل",
            "المرونة التقاطعية"
        ]

        PRICE1 = "السعر الابتدائي"
        PRICE2 = "السعر الجديد"

        INCOME1 = "الدخل الابتدائي"
        INCOME2 = "الدخل الجديد"

        RESULT = "قيمة المرونة"
        INTERPRET = "التفسير"

        ELASTIC = "طلب مرن"
        INELASTIC = "طلب غير مرن"
        UNIT = "مرونة وحدوية"

        NORMAL = "سلعة عادية"
        INFERIOR = "سلعة دنيا"

        SUBSTITUTE = "سلع بديلة"
        COMPLEMENT = "سلع مكملة"

    st.title(TITLE)

    method = st.selectbox("Method" if lang=="English" else "اختر الطريقة", METHODS)

    # =====================================================
    # BASE DEMAND FUNCTION (Law of Demand)
    # Q = a − bP
    # =====================================================

    a = 200
    b = 3

    # =====================================================
    # PRICE ELASTICITY (LAW OF DEMAND ENFORCED)
    # =====================================================

    if method in METHODS[0:2]:

        P1 = st.slider(PRICE1, 1, 100, 20)
        P2 = st.slider(PRICE2, 1, 100, 40)

        # Quantity automatically determined by demand curve
        Q1 = a - b * P1
        Q2 = a - b * P2

        st.write(f"Q1 = {Q1}")
        st.write(f"Q2 = {Q2}")

        if method == METHODS[0]:

            elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

        else:

            elasticity = (
                ((Q2 - Q1) / ((Q1 + Q2) / 2)) /
                ((P2 - P1) / ((P1 + P2) / 2))
            )

    # =====================================================
    # INCOME ELASTICITY
    # =====================================================

    elif method == METHODS[2]:

        I1 = st.slider(INCOME1, 1000, 10000, 3000)
        I2 = st.slider(INCOME2, 1000, 10000, 5000)

        # Assume demand increases with income (normal good)
        Q1 = 100 + 0.02 * I1
        Q2 = 100 + 0.02 * I2

        st.write(f"Q1 = {int(Q1)}")
        st.write(f"Q2 = {int(Q2)}")

        elasticity = ((Q2 - Q1) / Q1) / ((I2 - I1) / I1)

    # =====================================================
    # CROSS PRICE ELASTICITY
    # =====================================================

    elif method == METHODS[3]:

        P1 = st.slider("Initial price of other good", 1, 100, 20)
        P2 = st.slider("New price of other good", 1, 100, 40)

        # Assume substitute relationship
        Q1 = 50 + 2 * P1
        Q2 = 50 + 2 * P2

        st.write(f"Q1 = {Q1}")
        st.write(f"Q2 = {Q2}")

        elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

    # =====================================================
    # RESULT
    # =====================================================

    st.metric(RESULT, round(elasticity, 3))

    st.subheader(INTERPRET)

    if method in METHODS[0:2]:

        if abs(elasticity) > 1:
            st.success(ELASTIC)
        elif abs(elasticity) < 1:
            st.warning(INELASTIC)
        else:
            st.info(UNIT)

    elif method == METHODS[2]:

        if elasticity > 0:
            st.success(NORMAL)
        else:
            st.warning(INFERIOR)

    elif method == METHODS[3]:

        if elasticity > 0:
            st.success(SUBSTITUTE)
        else:
            st.warning(COMPLEMENT)
# =========================
    # SHOW FORMULA
    # =========================

    with st.expander("Show formula" if lang=="English" else "عرض الصيغة"):

        if method == METHODS[0]:

            st.latex(r"E = \frac{\%\Delta Q}{\%\Delta P}")

        elif method == METHODS[1]:

            st.latex(
                r"E = \frac{(Q2-Q1)/((Q1+Q2)/2)}{(P2-P1)/((P1+P2)/2)}"
            )

        elif method == METHODS[2]:

            st.latex(r"E = \frac{\%\Delta Q}{\%\Delta Income}")

        elif method == METHODS[3]:

            st.latex(r"E = \frac{\%\Delta Q_A}{\%\Delta P_B}")
