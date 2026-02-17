import streamlit as st


def run(lang="English"):

    # =====================
    # LANGUAGE TEXT
    # =====================

    if lang == "English":

        TITLE = "Elasticity Simulator"
        METHOD_LABEL = "Select elasticity type"

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

        ELASTIC = "Elastic demand"
        INELASTIC = "Inelastic demand"
        UNIT = "Unit elastic demand"

        NORMAL = "Normal good"
        INFERIOR = "Inferior good"

        SUBSTITUTE = "Substitute goods"
        COMPLEMENT = "Complement goods"

    else:

        TITLE = "محاكي المرونة"
        METHOD_LABEL = "اختر نوع المرونة"

        METHODS = [
            "المرونة السعرية البسيطة",
            "مرونة نقطة الوسط",
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

    method = st.selectbox(METHOD_LABEL, METHODS)

    # =====================
    # DEMAND FUNCTION
    # =====================

    a = 200
    b = 3

    elasticity = 0.0

    # =====================
    # PRICE ELASTICITY
    # =====================

    if method in METHODS[0:2]:

        P1 = st.slider(PRICE1, 1, 100, 20)
        P2 = st.slider(PRICE2, 1, 100, 40)

        Q1 = max(1, a - b * P1)
        Q2 = max(1, a - b * P2)

        st.write("Quantity at P1:", Q1)
        st.write("Quantity at P2:", Q2)

        if method == METHODS[0]:

            elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

        else:

            elasticity = (
                ((Q2 - Q1) / ((Q1 + Q2) / 2)) /
                ((P2 - P1) / ((P1 + P2) / 2))
            )

    # =====================
    # INCOME ELASTICITY
    # =====================

    elif method == METHODS[2]:

        I1 = st.slider(INCOME1, 1000, 10000, 3000)
        I2 = st.slider(INCOME2, 1000, 10000, 5000)

        Q1 = 50 + 0.02 * I1
        Q2 = 50 + 0.02 * I2

        st.write("Quantity at Income 1:", int(Q1))
        st.write("Quantity at Income 2:", int(Q2))

        elasticity = ((Q2 - Q1) / Q1) / ((I2 - I1) / I1)

    # =====================
    # CROSS ELASTICITY
    # =====================

    elif method == METHODS[3]:

        P1 = st.slider("Other good price 1", 1, 100, 20)
        P2 = st.slider("Other good price 2", 1, 100, 40)

        Q1 = 40 + 2 * P1
        Q2 = 40 + 2 * P2

        st.write("Quantity:", Q1, "→", Q2)

        elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

    # =====================
    # SHOW RESULT
    # =====================

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
