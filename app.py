import streamlit as st

from modules import supply_demand
from modules import elasticity
from modules import production_cost
from modules import quiz

st.set_page_config(page_title="Microeconomics Platform")

st.title("Microeconomics Interactive Platform")

menu = st.sidebar.selectbox(
    "Choose chapter",
    [
        "Supply and Demand",
        "Elasticity",
        "Production and Cost",
        "Quiz"
    ]
)

if menu == "Supply and Demand":
    supply_demand.run()

elif menu == "Elasticity":
    elasticity.run()

elif menu == "Production and Cost":
    production_cost.run()

elif menu == "Quiz":
    quiz.run()
