import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run():

    st.header("🏭 دالة الإنتاج")

    L = np.linspace(1, 50, 100)

    A = st.slider("مستوى التكنولوجيا (A)", 1, 5, 2)
    alpha = st.slider("مرونة العمل (α)", 0.1, 0.9, 0.5)

    Q = A * (L ** alpha)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=L, y=Q, name="الإنتاج"))

    fig.update_layout(
        xaxis_title="العمل",
        yaxis_title="الإنتاج"
    )

    st.plotly_chart(fig, use_container_width=True)
