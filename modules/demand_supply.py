import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from utils import calculate_equilibrium

def run(lang="English"):
    # -----------------------------
    # Page Header
    # -----------------------------
    st.header("Demand & Supply" if lang=="English" else "العرض والطلب")

    st.write(
        "Adjust the sliders to simulate demand and supply curves." 
        if lang=="English" 
        else "غيّر القيم في الشرائح لمحاكاة منحنيات العرض والطلب."
    )

    # -----------------------------
    # Sliders for Parameters
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        a = st.slider("Demand Intercept (a)", 50, 200, 120)
        b = st.slider("Demand Slope (b)", 1, 10, 3)

    with col2:
        c = st.slider("Supply Intercept (c)", 0, 100, 20)
        d = st.slider("Supply Slope (d)", 1, 10, 2)

    # -----------------------------
    # Calculate Equilibrium
    # -----------------------------
    eq_price, eq_quantity = calculate_equilibrium(a, b, c, d)
    st.success(
        f"Equilibrium Price = {eq_price:.2f} | Quantity = {eq_quantity:.2f}"
        if lang=="English" 
        else f"سعر التوازن = {eq_price:.2f} | الكمية = {eq_quantity:.2f}"
    )

    # -----------------------------
    # Generate Demand & Supply Data
    # -----------------------------
    prices = np.linspace(0, eq_price*2, 50)
    demand = a - b*prices
    supply = c + d*prices

    df = pd.DataFrame({
        "Price": prices,
        "Demand": demand,
        "Supply": supply
    })

    # -----------------------------
    # Plot Interactive Graph
    # -----------------------------
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Quantity"], y=df["Price"], mode='lines', name="Supply"))
    fig.add_trace(go.Scatter(x=df["Quantity"], y=df["Price"], mode='lines', name="Demand"))

    fig.add_trace(go.Scatter(
        x=[eq_quantity], y=[eq_price],
        mode='markers+text',
        name="Equilibrium",
        marker=dict(color='red', size=12),
        text=["Equilibrium"],
        textposition="top right"
    ))

    fig.update_layout(
        title="Demand & Supply Curve" if lang=="English" else "منحنيات العرض والطلب",
        xaxis_title="Quantity" if lang=="English" else "الكمية",
        yaxis_title="Price" if lang=="English" else "السعر",
        legend_title="Legend" if lang=="English" else "المفتاح",
        width=800, height=500
    )

    st.plotly_chart(fig)

    # -----------------------------
    # Optional Scenario Simulation
    # -----------------------------
    st.subheader("Scenario Simulation" if lang=="English" else "محاكاة سيناريو")
    st.write(
        "Adjust supply or demand and see how equilibrium changes."
        if lang=="English" else
        "غيّر العرض أو الطلب وشاهد كيف يتغير التوازن."
    )

    shift_type = st.radio(
        "Shift Type" if lang=="English" else "نوع التغير",
        ["Increase Demand", "Decrease Demand", "Increase Supply", "Decrease Supply"]
        if lang=="English" else
        ["زيادة الطلب", "انخفاض الطلب", "زيادة العرض", "انخفاض العرض"]
    )

    shift_value = st.slider(
        "Shift magnitude", 0, 50, 10
        if lang=="English" else
        "مقدار التغير", 0, 50, 10
    )

    # Apply shift
    new_a, new_c = a, c
    if shift_type in ["Increase Demand", "زيادة الطلب"]:
        new_a += shift_value
    elif shift_type in ["Decrease Demand", "انخفاض الطلب"]:
        new_a -= shift_value
    elif shift_type in ["Increase Supply", "زيادة العرض"]:
        new_c += shift_value
    elif shift_type in ["Decrease Supply", "انخفاض العرض"]:
        new_c -= shift_value

    new_eq_price, new_eq_quantity = calculate_equilibrium(new_a, b, new_c, d)
    st.info(
        f"New Equilibrium Price = {new_eq_price:.2f} | Quantity = {new_eq_quantity:.2f}"
        if lang=="English" else
        f"سعر التوازن الجديد = {new_eq_price:.2f} | الكمية = {new_eq_quantity:.2f}"
    )
