import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


def app():

    st.title("Demand and Supply Simulator")

    st.markdown("Visualize how demand and supply curves shift under different scenarios.")

    # -----------------------
    # Base parameters
    # -----------------------

    P = np.linspace(0, 20, 200)

    # Demand: Qd = a - bP
    a = 16
    b = 0.6

    # Supply: Qs = c + dP
    c = 2
    d = 0.5

    Qd = a - b * P
    Qs = c + d * P

    # -----------------------
    # Scenario selection
    # -----------------------

    scenario = st.selectbox(
        "Select scenario",
        [
            "No shock",
            "Increase in demand (income rise)",
            "Decrease in demand (pandemic)",
            "Increase in supply (technology improvement)",
            "Decrease in supply (war / cost increase)",
            "Supply increase (subsidy)"
        ]
    )

    # -----------------------
    # Shift values (different magnitudes)
    # -----------------------

    demand_shift = 0
    supply_shift = 0
    explanation = ""

    if scenario == "Increase in demand (income rise)":
        demand_shift = 3.0
        explanation = "Income rise increases demand. Demand curve shifts RIGHT."

    elif scenario == "Decrease in demand (pandemic)":
        demand_shift = -4.0
        explanation = "Pandemic reduces demand. Demand curve shifts LEFT."

    elif scenario == "Increase in supply (technology improvement)":
        supply_shift = 3.5
        explanation = "Technology improvement increases supply. Supply curve shifts RIGHT and DOWN."

    elif scenario == "Decrease in supply (war / cost increase)":
        supply_shift = -3.0
        explanation = "War increases costs. Supply curve shifts LEFT and UP."

    elif scenario == "Supply increase (subsidy)":
        supply_shift = 2.0
        explanation = "Subsidy reduces costs. Supply curve shifts RIGHT and DOWN."

    else:
        explanation = "No shock. Curves remain unchanged."

    # -----------------------
    # Apply shifts
    # -----------------------

    Qd_new = (a + demand_shift) - b * P
    Qs_new = (c + supply_shift) + d * P

    # -----------------------
    # Plot
    # -----------------------

    fig, ax = plt.subplots()

    # Original curves
    ax.plot(Qd, P, linewidth=3, label="Original Demand")
    ax.plot(Qs, P, linewidth=3, label="Original Supply")

    # New curves
    if demand_shift != 0:
        ax.plot(Qd_new, P, linestyle="--", linewidth=3, label="New Demand")

    if supply_shift != 0:
        ax.plot(Qs_new, P, linestyle="--", linewidth=3, label="New Supply")

    # -----------------------
    # Arrows
    # -----------------------

    if demand_shift > 0:
        arrow = FancyArrowPatch(
            (Qd[100], P[100]),
            (Qd_new[100], P[100]),
            arrowstyle="->",
            mutation_scale=20
        )
        ax.add_patch(arrow)

    if demand_shift < 0:
        arrow = FancyArrowPatch(
            (Qd[100], P[100]),
            (Qd_new[100], P[100]),
            arrowstyle="->",
            mutation_scale=20
        )
        ax.add_patch(arrow)

    if supply_shift > 0:
        arrow = FancyArrowPatch(
            (Qs[100], P[100]),
            (Qs_new[100], P[100]),
            arrowstyle="->",
            mutation_scale=20
        )
        ax.add_patch(arrow)

    if supply_shift < 0:
        arrow = FancyArrowPatch(
            (Qs[100], P[100]),
            (Qs_new[100], P[100]),
            arrowstyle="->",
            mutation_scale=20
        )
        ax.add_patch(arrow)

    # -----------------------
    # Labels
    # -----------------------

    ax.set_xlabel("Quantity")
    ax.set_ylabel("Price")
    ax.set_title("Demand and Supply Shift Simulation")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

    # -----------------------
    # Explanation box
    # -----------------------

    st.info(explanation)

    # -----------------------
    # Economic interpretation
    # -----------------------

    if demand_shift > 0:
        st.success("Result: Price increases and Quantity increases.")

    elif demand_shift < 0:
        st.warning("Result: Price decreases and Quantity decreases.")

    elif supply_shift > 0:
        st.success("Result: Price decreases and Quantity increases.")

    elif supply_shift < 0:
        st.warning("Result: Price increases and Quantity decreases.")
