import streamlit as st
import numpy as np
import plotly.graph_objects as go

# =====================================================
# BASE MARKET (FIXED)
# =====================================================

BASE_DEMAND = 120
BASE_SUPPLY = 20
SLOPE = 2


# =====================================================
# SHIFT VALUES (different magnitude)
# =====================================================

DEMAND_SHIFTS = {
    "No change": 0,
    "Income increase": 25,
    "Income decrease": -18,
    "Population increase": 30,
    "Population decrease": -22,
    "Price of substitute increases": 15,
    "Price of complement increases": -12,
    "Pandemic (restaurants closed)": -35,
}

SUPPLY_SHIFTS = {
    "No change": 0,
    "Technology improvement": 28,
    "Input cost increase": -26,
    "Government subsidy": 20,
    "New firms enter market": 18,
    "War (energy cost shock)": -40,
    "Tax increase": -22,
}


# =====================================================
# EXPLANATIONS
# =====================================================

DEMAND_EXPLANATION = {
    "Income increase": "Demand shifts RIGHT because consumers can buy more.",
    "Income decrease": "Demand shifts LEFT because consumers have less purchasing power.",
    "Population increase": "Demand shifts RIGHT because there are more buyers.",
    "Population decrease": "Demand shifts LEFT because there are fewer buyers.",
    "Price of substitute increases": "Demand shifts RIGHT because substitute becomes expensive.",
    "Price of complement increases": "Demand shifts LEFT because complement becomes expensive.",
    "Pandemic (restaurants closed)": "Demand shifts LEFT due to economic shutdown.",
    "No change": "Demand curve does not shift."
}

SUPPLY_EXPLANATION = {
    "Technology improvement": "Supply shifts RIGHT because production becomes cheaper.",
    "Input cost increase": "Supply shifts LEFT because production becomes more expensive.",
    "Government subsidy": "Supply shifts RIGHT because producers receive financial support.",
    "New firms enter market": "Supply shifts RIGHT because more producers exist.",
    "War (energy cost shock)": "Supply shifts LEFT because production costs increase sharply.",
    "Tax increase": "Supply shifts LEFT because producers face higher costs.",
    "No change": "Supply curve does not shift."
}


# =====================================================
# MAIN FUNCTION
# =====================================================

def run(lang="English"):

    st.header("Demand & Supply Simulator")

    # =================================================
    # MODE SELECTION
    # =================================================

    mode = st.radio(
        "Select simulation mode:",
        [
            "1. Demand shift (Supply constant)",
            "2. Supply shift (Demand constant)"
        ]
    )

    prices = np.linspace(0, 100, 200)

    original_demand = BASE_DEMAND - SLOPE * prices
    original_supply = BASE_SUPPLY + SLOPE * prices


    # =================================================
    # DEMAND SHIFT MODE
    # =================================================

    if mode.startswith("1"):

        factor = st.selectbox(
            "Select demand factor:",
            list(DEMAND_SHIFTS.keys())
        )

        shift = DEMAND_SHIFTS[factor]

        new_demand_intercept = BASE_DEMAND + shift

        new_demand = new_demand_intercept - SLOPE * prices
        new_supply = original_supply


        # equilibrium
        eq_price = (new_demand_intercept - BASE_SUPPLY) / (2 * SLOPE)
        eq_quantity = new_demand_intercept - SLOPE * eq_price


        # =================================================
        # EXPLANATION BOX
        # =================================================

        st.info(DEMAND_EXPLANATION[factor])

        direction = "RIGHT ➜" if shift > 0 else "LEFT ⬅"


        # =================================================
        # GRAPH
        # =================================================

        fig = go.Figure()

        # original curves (thin dashed)
        fig.add_trace(go.Scatter(
            x=prices,
            y=original_demand,
            name="Original Demand",
            line=dict(dash="dash", width=2, color="blue")
        ))

        fig.add_trace(go.Scatter(
            x=prices,
            y=original_supply,
            name="Supply (constant)",
            line=dict(width=3, color="red")
        ))

        # new demand curve (thick)
        fig.add_trace(go.Scatter(
            x=prices,
            y=new_demand,
            name="New Demand",
            line=dict(width=4, color="green")
        ))


        # arrow annotation
        fig.add_annotation(
            x=60,
            y=new_demand_intercept,
            text=f"Demand shifts {direction}",
            showarrow=True,
            arrowhead=3,
            font=dict(size=16, color="green")
        )


    # =================================================
    # SUPPLY SHIFT MODE
    # =================================================

    else:

        factor = st.selectbox(
            "Select supply factor:",
            list(SUPPLY_SHIFTS.keys())
        )

        shift = SUPPLY_SHIFTS[factor]

        new_supply_intercept = BASE_SUPPLY + shift

        new_supply = new_supply_intercept + SLOPE * prices
        new_demand = original_demand


        eq_price = (BASE_DEMAND - new_supply_intercept) / (2 * SLOPE)
        eq_quantity = BASE_DEMAND - SLOPE * eq_price


        st.info(SUPPLY_EXPLANATION[factor])

        direction = "RIGHT ➜" if shift > 0 else "LEFT ⬅"


        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=prices,
            y=original_supply,
            name="Original Supply",
            line=dict(dash="dash", width=2, color="red")
        ))

        fig.add_trace(go.Scatter(
            x=prices,
            y=original_demand,
            name="Demand (constant)",
            line=dict(width=3, color="blue")
        ))

        fig.add_trace(go.Scatter(
            x=prices,
            y=new_supply,
            name="New Supply",
            line=dict(width=4, color="green")
        ))

        fig.add_annotation(
            x=60,
            y=new_supply_intercept,
            text=f"Supply shifts {direction}",
            showarrow=True,
            arrowhead=3,
            font=dict(size=16, color="green")
        )


    # =================================================
    # EQUILIBRIUM DISPLAY
    # =================================================

    st.success(f"New Equilibrium Price: {eq_price:.2f}")
    st.success(f"New Equilibrium Quantity: {eq_quantity:.2f}")


    # =================================================
    # FINAL GRAPH SETTINGS
    # =================================================

    fig.update_layout(
        title="Market Shock Simulation",
        xaxis_title="Price",
        yaxis_title="Quantity",
        legend=dict(font=dict(size=14))
    )

    st.plotly_chart(fig, use_container_width=True)
