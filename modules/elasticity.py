import streamlit as st

def run(lang="English"):
    st.header("Elasticity" if lang=="English" else "المرونة")

    st.write(
        "Calculate price elasticity of demand by adjusting prices and quantities."
        if lang=="English"
        else "احسب مرونة الطلب السعرية عن طريق تغيير الأسعار والكميات."
    )

    # Input sliders
    P1 = st.slider("Initial Price (P1)", 1, 100, 20)
    P2 = st.slider("New Price (P2)", 1, 100, 30)

    Q1 = st.slider("Initial Quantity (Q1)", 10, 200, 100)
    Q2 = st.slider("New Quantity (Q2)", 10, 200, 70)

    # Elasticity calculation (midpoint method)
    try:
        elasticity = ((Q2 - Q1) / ((Q1 + Q2) / 2)) / ((P2 - P1) / ((P1 + P2) / 2))
        elasticity_rounded = round(elasticity, 2)
    except ZeroDivisionError:
        elasticity_rounded = None

    if elasticity_rounded is not None:
        st.metric("Elasticity" if lang=="English" else "المرونة", elasticity_rounded)
        if elasticity_rounded > 1:
            st.info("Demand is Elastic" if lang=="English" else "الطلب مرن")
        elif elasticity_rounded < 1:
            st.info("Demand is Inelastic" if lang=="English" else "الطلب غير مرن")
        else:
            st.info("Unit Elastic Demand" if lang=="English" else "الطلب متساوي المرونة")
    else:
        st.error("Invalid inputs for calculation" if lang=="English" else "قيم غير صالحة للحساب")
