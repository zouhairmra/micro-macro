import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def run(lang="English"):
    st.header("Demand & Supply" if lang=="English" else "العرض والطلب")

    col1, col2 = st.columns(2)
    with col1:
        a = st.slider("Demand intercept", 50, 200, 120)
        b = st.slider("Demand slope", 1, 10, 3)
    with col2:
        c = st.slider("Supply intercept", 0, 100, 20)
        d = st.slider("Supply slope", 1, 10, 2)

    eq_price = (a-c)/(b+d)
    eq_quantity = a - b*eq_price

    st.success(f"Equilibrium Price = {eq_price:.2f} | Quantity = {eq_quantity:.2f}")

    prices = np.linspace(0, eq_price*2, 50)
    demand = a - b*prices
    supply = c + d*prices

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=prices, y=demand, mode='lines', name="Demand"))
    fig.add_trace(go.Scatter(x=prices, y=supply, mode='lines', name="Supply"))
    fig.update_layout(xaxis_title="Price", yaxis_title="Quantity")
    st.plotly_chart(fig, use_container_width=True)
