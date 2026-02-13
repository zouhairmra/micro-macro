import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run(lang="English"):
    st.header("Elasticity" if lang=="English" else "المرونة")
    st.write(
        "Calculate price elasticity of demand and visualize changes."
        if lang=="English"
        else "احسب مرونة الطلب السعرية وشاهد التغيرات بصريًا."
    )

    # -----------------------------
    # Input Sliders
    # -----------------------------
    col1, col2 = st.columns(2)
    with col1:
        P1 = st.slider("Initial Price (P1)", 1, 100, 20)
        P2 = st.slider("New Price (P2)", 1, 100, 30)
    with col2:
        Q1 = st.slider("Initial Quantity (Q1)", 10, 200, 100)
        Q2 = st.slider("New Quantity (Q2)", 10, 200, 70)

    # -----------------------------
    # Elasticity Calculation (Midpoint)
    # -----------------------------
    try:
        elasticity = ((Q2 - Q1) / ((Q1 + Q2) / 2)) / ((P2 - P1) / ((P1 + P2) / 2))
        elasticity_rounded = round(elasticity, 2)
    except ZeroDivisionError:
        elasticity_rounded = None

    # -----------------------------
    # Display Result
    # -----------------------------
    if elasticity_rounded is not None:
        st.metric("Elasticity" if lang=="English" else "المرونة", elasticity_rounded)

        if elasticity_rounded > 1:
            status = "Elastic" if lang=="English" else "مرن"
        elif elasticity_rounded < 1:
            status = "Inelastic" if lang=="English" else "غير مرن"
        else:
            status = "Unit Elastic" if lang=="English" else "متساوي المرونة"

        st.info(f"Demand is {status}" if lang=="English" else f"الطلب {status}")
    else:
        st.error("Invalid input values" if lang=="English" else "قيم الإدخال غير صالحة")

    # -----------------------------
    # Plot Elasticity Graph
    # -----------------------------
    prices = np.array([P1, P2])
    quantities = np.array([Q1, Q2])

    fig = go.Figure()

    # Demand line connecting the two points
    fig.add_trace(go.Scatter(
        x=quantities, y=prices, mode='lines+markers',
        line=dict(color='blue', width=3),
        marker=dict(size=10),
        name="Demand Curve" if lang=="English" else "منحنى الطلب"
    ))

    # Highlight points
    fig.add_trace(go.Scatter(
        x=[Q1], y=[P1], mode='markers+text',
        marker=dict(color='green', size=12),
        text=["P1,Q1"], textposition="top right",
        name="Initial Point" if lang=="English" else "النقطة الأولى"
    ))

    fig.add_trace(go.Scatter(
        x=[Q2], y=[P2], mode='markers+text',
        marker=dict(color='red', size=12),
        text=["P2,Q2"], textposition="top right",
        name="New Point" if lang=="English" else "النقطة الجديدة"
    ))

    fig.update_layout(
        title="Elasticity Visualization" if lang=="English" else "تمثيل المرونة السعرية",
        xaxis_title="Quantity" if lang=="English" else "الكمية",
        yaxis_title="Price" if lang=="English" else "السعر",
        width=800, height=500
    )

    st.plotly_chart(fig)

    # -----------------------------
    # Optional: Interactive What-If
    # -----------------------------
    st.subheader("What-If Analysis" if lang=="English" else "تحليل ماذا لو")
    st.write(
        "Adjust prices or quantities to see how elasticity changes."
        if lang=="English"
        else "غيّر الأسعار أو الكميات لملاحظة التغير في المرونة."
    )
