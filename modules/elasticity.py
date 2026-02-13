import streamlit as st

def run(lang="English"):
    st.header("Elasticity" if lang=="English" else "المرونة")

    P1 = st.slider("Initial Price", 1, 100, 20)
    P2 = st.slider("New Price", 1, 100, 30)
    Q1 = st.slider("Initial Quantity", 10, 200, 100)
    Q2 = st.slider("New Quantity", 10, 200, 70)

    elasticity = ((Q2-Q1)/((Q1+Q2)/2)) / ((P2-P1)/((P1+P2)/2))
    st.metric("Elasticity", round(elasticity,2))
