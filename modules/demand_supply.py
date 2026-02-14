import streamlit as st
import numpy as np
import plotly.graph_objects as go


def run(lang="English"):

    title = "Demand and Supply Simulator" if lang == "English" else "محاكي العرض والطلب"
    st.title(title)

    P = np.linspace(0, 20, 200)

    # Base equations
    a = 16
    b = 0.6
    c = 2
    d = 0.5

    Qd = a - b * P
    Qs = c + d * P

    scenario = st.selectbox(
        "Select scenario" if lang == "English" else "اختر السيناريو",
        [
            "No shock",
            "Increase in demand (income rise)",
            "Decrease in demand (pandemic)",
            "Increase in supply (technology improvement)",
            "Decrease in supply (war / cost increase)",
            "Supply increase (subsidy)"
        ]
    )

    demand_shift = 0
    supply_shift = 0
    explanation = ""

    if scenario == "Increase in demand (income rise)":
        demand_shift = 3
        explanation = "Income rise → Demand shifts RIGHT."

    elif scenario == "Decrease in demand (pandemic)":
        demand_shift = -4
        explanation = "Pandemic → Demand shifts LEFT."

    elif scenario == "Increase in supply (technology improvement)":
        supply_shift = 3.5
        explanation = "Technology improvement → Supply shifts RIGHT (downward)."

    elif scenario == "Decrease in supply (war / cost increase)":
        supply_shift = -3
        explanation = "War increases costs → Supply shifts LEFT (upward)."

    elif scenario == "Supply increase (subsidy)":
        supply_shift = 2
        explanation = "Subsidy → Supply shifts RIGHT."

    Qd_new = (a + demand_shift) - b * P
    Qs_new = (c + supply_shift) + d * P

    fig = go.Figure()

    # Original curves
    fig.add_trace(go.Scatter(
        x=Qd,
        y=P,
        mode='lines',
        name="Original Demand"
    ))

    fig.add_trace(go.Scatter(
        x=Qs,
        y=P,
        mode='lines',
        name="Original Supply"
    ))

    # Shifted curves
    if demand_shift != 0:
        fig.add_trace(go.Scatter(
            x=Qd_new,
            y=P,
            mode='lines',
            name="New Demand",
            line=dict(dash="dash")
        ))

    if supply_shift != 0:
        fig.add_trace(go.Scatter(
            x=Qs_new,
            y=P,
            mode='lines',
            name="New Supply",
            line=dict(dash="dash")
        ))

    fig.update_layout(
        xaxis_title="Quantity",
        yaxis_title="Price",
        template="simple_white"
    )

    st.plotly_chart(fig, use_container_width=True)

    if explanation:
        st.info(explanation)

    if demand_shift > 0:
        st.success("Price ↑ Quantity ↑")

    elif demand_shift < 0:
        st.warning("Price ↓ Quantity ↓")

    elif supply_shift > 0:
        st.success("Price ↓ Quantity ↑")

    elif supply_shift < 0:
        st.warning("Price ↑ Quantity ↓")
