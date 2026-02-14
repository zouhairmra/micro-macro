import streamlit as st
import numpy as np
import plotly.graph_objects as go


def run(lang="English"):

    # =========================
    # LANGUAGE TEXT
    # =========================

    if lang == "English":

        TITLE = "Demand and Supply Interactive Simulator"
        SCENARIO_LABEL = "Select economic shock"
        EXPLANATION_TITLE = "Economic explanation"
        RESULT_TITLE = "Market result"
        EQUILIBRIUM_TITLE = "Equilibrium"

    else:

        TITLE = "محاكي العرض والطلب التفاعلي"
        SCENARIO_LABEL = "اختر الصدمة الاقتصادية"
        EXPLANATION_TITLE = "التفسير الاقتصادي"
        RESULT_TITLE = "نتيجة السوق"
        EQUILIBRIUM_TITLE = "التوازن"

    st.title(TITLE)

    # =========================
    # BASE MARKET
    # =========================

    P = np.linspace(0, 20, 200)

    # Demand: Qd = a − bP
    a = 16
    b = 0.6

    # Supply: Qs = c + dP
    c = 2
    d = 0.5

    Qd = a - b * P
    Qs = c + d * P

    # =========================
    # SCENARIOS
    # =========================

    scenario = st.selectbox(

        SCENARIO_LABEL,

        [

            "No shock",

            "Demand increase (income rise)",

            "Demand decrease (pandemic)",

            "Supply increase (technology)",

            "Supply decrease (war)",

            "Supply increase (subsidy)",

            "Supply decrease (tax)"

        ]

    )

    demand_shift = 0
    supply_shift = 0
    explanation = ""

    # Demand shocks
    if scenario == "Demand increase (income rise)":

        demand_shift = 4

        explanation = "Higher income increases demand → demand curve shifts RIGHT"

    elif scenario == "Demand decrease (pandemic)":

        demand_shift = -5

        explanation = "Pandemic reduces consumption → demand shifts LEFT"

    # Supply shocks
    elif scenario == "Supply increase (technology)":

        supply_shift = 4

        explanation = "Technology reduces cost → supply shifts RIGHT (DOWN)"

    elif scenario == "Supply decrease (war)":

        supply_shift = -4

        explanation = "War increases cost → supply shifts LEFT (UP)"

    elif scenario == "Supply increase (subsidy)":

        supply_shift = 3

        explanation = "Subsidy reduces cost → supply shifts RIGHT"

    elif scenario == "Supply decrease (tax)":

        supply_shift = -3

        explanation = "Tax increases cost → supply shifts LEFT"

    # =========================
    # NEW CURVES
    # =========================

    Qd_new = (a + demand_shift) - b * P
    Qs_new = (c + supply_shift) + d * P

    # =========================
    # EQUILIBRIUM
    # =========================

    def equilibrium(a, b, c, d):

        Pe = (a - c) / (b + d)
        Qe = a - b * Pe

        return Pe, Qe

    Pe, Qe = equilibrium(a, b, c, d)

    Pe_new, Qe_new = equilibrium(
        a + demand_shift,
        b,
        c + supply_shift,
        d
    )

    # =========================
    # GRAPH
    # =========================

    fig = go.Figure()

    # Original curves
    fig.add_trace(go.Scatter(

        x=Qd,
        y=P,
        name="Original Demand",
        line=dict(width=4)

    ))

    fig.add_trace(go.Scatter(

        x=Qs,
        y=P,
        name="Original Supply",
        line=dict(width=4)

    ))

    # New curves
    if demand_shift != 0:

        fig.add_trace(go.Scatter(

            x=Qd_new,
            y=P,
            name="New Demand",
            line=dict(dash="dash", width=4)

        ))

    if supply_shift != 0:

        fig.add_trace(go.Scatter(

            x=Qs_new,
            y=P,
            name="New Supply",
            line=dict(dash="dash", width=4)

        ))

    # Equilibrium points

    fig.add_trace(go.Scatter(

        x=[Qe],
        y=[Pe],
        mode="markers",
        marker=dict(size=12),
        name="Original Equilibrium"

    ))

    if scenario != "No shock":

        fig.add_trace(go.Scatter(

            x=[Qe_new],
            y=[Pe_new],
            mode="markers",
            marker=dict(size=12),
            name="New Equilibrium"

        ))

    # Arrow showing shift

    if scenario != "No shock":

        fig.add_annotation(

            x=Qe_new,
            y=Pe_new,
            ax=Qe,
            ay=Pe,
            showarrow=True,
            arrowhead=3,
            arrowsize=2,
            arrowwidth=2

        )

    fig.update_layout(

        xaxis_title="Quantity",
        yaxis_title="Price",
        template="simple_white",
        height=600

    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # EQUILIBRIUM DISPLAY
    # =========================

    st.subheader(EQUILIBRIUM_TITLE)

    col1, col2 = st.columns(2)

    col1.metric("Original Price", round(Pe, 2))
    col1.metric("Original Quantity", round(Qe, 2))

    col2.metric("New Price", round(Pe_new, 2))
    col2.metric("New Quantity", round(Qe_new, 2))

    # =========================
    # EXPLANATION BOX
    # =========================

    st.subheader(EXPLANATION_TITLE)

    st.info(explanation)

    # =========================
    # RESULT INTERPRETATION
    # =========================

    st.subheader(RESULT_TITLE)

    if Pe_new > Pe:

        price_result = "Price increases"

    else:

        price_result = "Price decreases"

    if Qe_new > Qe:

        quantity_result = "Quantity increases"

    else:

        quantity_result = "Quantity decreases"

    st.success(f"{price_result} and {quantity_result}")
