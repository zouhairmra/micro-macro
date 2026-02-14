import streamlit as st


def run(lang="English"):

    # =========================
    # LANGUAGE
    # =========================

    if lang == "English":

        TITLE = "Elasticity Simulator"

        METHODS = [
            "Standard Price Elasticity",
            "Midpoint Elasticity",
            "Income Elasticity",
            "Cross-Price Elasticity"
        ]

        PRICE1 = "Initial Price"
        PRICE2 = "New Price"
        Q1_TEXT = "Initial Quantity"
        Q2_TEXT = "New Quantity"

        INCOME1 = "Initial Income"
        INCOME2 = "New Income"

        OTHER_PRICE1 = "Initial Price of Other Good"
        OTHER_PRICE2 = "New Price of Other Good"

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

        TITLE = "محاكي المرونة"

        METHODS = [
            "المرونة السعرية (الطريقة البسيطة)",
            "المرونة السعرية (طريقة نقطة الوسط)",
            "مرونة الدخل",
            "المرونة التقاطعية"
        ]

        PRICE1 = "السعر الابتدائي"
        PRICE2 = "السعر الجديد"
        Q1_TEXT = "الكمية الابتدائية"
        Q2_TEXT = "الكمية الجديدة"

        INCOME1 = "الدخل الابتدائي"
        INCOME2 = "الدخل الجديد"

        OTHER_PRICE1 = "السعر الابتدائي للسلعة الأخرى"
        OTHER_PRICE2 = "السعر الجديد للسلعة الأخرى"

        RESULT = "قيمة المرونة"

        INTERPRET = "التفسير"

        ELASTIC = "طلب مرن"
        INELASTIC = "طلب غير مرن"
        UNIT = "مرونة وحدوية"

        NORMAL = "سلعة عادية"
        INFERIOR = "سلعة دنيا"

        SUBSTITUTE = "سلع بديلة"
        COMPLEMENT = "سلع مكملة"

    # =========================
    # TITLE
    # =========================

    st.title(TITLE)

    # =========================
    # METHOD SELECTION
    # =========================

    method = st.selectbox("Method" if lang=="English" else "اختر الطريقة", METHODS)

    # =========================
    # COMMON INPUTS
    # =========================

    Q1 = st.slider(Q1_TEXT, 1, 500, 100)
    Q2 = st.slider(Q2_TEXT, 1, 500, 80)

    # =========================
    # STANDARD ELASTICITY
    # =========================

    if method == METHODS[0]:

        P1 = st.slider(PRICE1, 1, 200, 20)
        P2 = st.slider(PRICE2, 1, 200, 30)

        elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

    # =========================
    # MIDPOINT METHOD
    # =========================

    elif method == METHODS[1]:

        P1 = st.slider(PRICE1, 1, 200, 20)
        P2 = st.slider(PRICE2, 1, 200, 30)

        elasticity = (
            ((Q2 - Q1) / ((Q1 + Q2) / 2)) /
            ((P2 - P1) / ((P1 + P2) / 2))
        )

    # =========================
    # INCOME ELASTICITY
    # =========================

    elif method == METHODS[2]:

        I1 = st.slider(INCOME1, 100, 10000, 2000)
        I2 = st.slider(INCOME2, 100, 10000, 3000)

        elasticity = ((Q2 - Q1) / Q1) / ((I2 - I1) / I1)

    # =========================
    # CROSS PRICE ELASTICITY
    # =========================

    elif method == METHODS[3]:

        P1 = st.slider(OTHER_PRICE1, 1, 200, 20)
        P2 = st.slider(OTHER_PRICE2, 1, 200, 40)

        elasticity = ((Q2 - Q1) / Q1) / ((P2 - P1) / P1)

    # =========================
    # RESULT DISPLAY
    # =========================

    st.metric(RESULT, round(elasticity, 3))

    # =========================
    # INTERPRETATION
    # =========================

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
