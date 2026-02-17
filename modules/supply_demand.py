import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run():

    st.header("📈 العرض والطلب")

    st.write("""
    يوضح هذا النموذج العلاقة بين السعر والكمية المطلوبة والمعروضة.
    """)

    a = st.slider("ثابت الطلب (a)", 5, 30, 20)
    b = st.slider("ميل الطلب (b)", 1, 5, 2)

    c = st.slider("ثابت العرض (c)", 0, 20, 5)
    d = st.slider("ميل العرض (d)", 1, 5, 2)

    P = np.linspace(0, 20, 100)

    Qd = a - b*P
    Qs = c + d*P

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=Qd, y=P, name="الطلب"))
    fig.add_trace(go.Scatter(x=Qs, y=P, name="العرض"))

    fig.update_layout(
        xaxis_title="الكمية",
        yaxis_title="السعر"
    )

    st.plotly_chart(fig, use_container_width=True)
