import streamlit as st
import numpy as np
import plotly.graph_objects as go

def run(lang="English"):

    st.header("Demand & Supply – Market Shifts" if lang=="English" else "العرض والطلب – تحولات السوق")

    # =====================================
    # Base Market (fixed equations)
    # Qd = 120 - 2P
    # Qs = 20 + 2P
    # =====================================
    base_demand_intercept = 120
    base_supply_intercept = 20
    slope = 2

    # =====================================
    # DEMAND FACTORS
    # =====================================
    st.subheader("Demand Shifters" if lang=="English" else "عوامل تحول الطلب")

    demand_factor = st.selectbox(
        "Select a demand factor:" if lang=="English" else "اختر عامل يؤثر على الطلب:",
        [
            "No Change",
            "Increase in Income",
            "Decrease in Income",
            "Increase in Population",
            "Decrease in Population",
            "Increase in Price of Substitute",
            "Increase in Price of Complement"
        ] if lang=="English" else
        [
            "لا تغيير",
            "زيادة الدخل",
            "انخفاض الدخل",
            "زيادة عدد السكان",
            "انخفاض عدد السكان",
            "زيادة سعر سلعة بديلة",
            "زيادة سعر سلعة مكملة"
        ]
    )

    demand_shift = 0

    if demand_factor in ["Increase in Income","Increase in Population","Increase in Price of Substitute",
                         "زيادة الدخل","زيادة عدد السكان","زيادة سعر سلعة بديلة"]:
        demand_shift = 20

    if demand_factor in ["Decrease in Income","Decrease in Population","Increase in Price of Complement",
                         "انخفاض الدخل","انخفاض عدد السكان","زيادة سعر سلعة مكملة"]:
        demand_shift = -20

    # =====================================
    # SUPPLY FACTORS
    # =====================================
    st.subheader("Supply Shifters" if lang=="English" else "عوامل تحول العرض")

    supply_factor = st.selectbox(
        "Select a supply factor:" if lang=="English" else "اختر عامل يؤثر على العرض:",
        [
            "No Change",
            "Improvement in Technology",
            "Increase in Input Costs",
            "Government Subsidy",
            "Increase in Taxes",
            "Increase in Number of Sellers"
        ] if lang=="English" else
        [
            "لا تغيير",
            "تحسن التكنولوجيا",
            "زيادة تكاليف الإنتاج",
            "دعم حكومي",
            "زيادة الضرائب",
            "زيادة عدد المنتجين"
        ]
    )

    supply_shift = 0

    if supply_factor in ["Improvement in Technology","Government Subsidy","Increase in Number of Sellers",
                         "تحسن التكنولوجيا","دعم حكومي","زيادة عدد المنتجين"]:
        supply_shift = 20

    if supply_factor in ["Increase in Input Costs","Increase in Taxes",
                         "زيادة تكاليف الإنتاج","زيادة الضرائب"]:
        supply_shift = -20

    # =====================================
    # New Equations after shifts
    # =====================================
    new_demand_intercept = base_demand_intercept + demand_shift
    new_supply_intercept = base_supply_intercept + supply_shift

    # Equilibrium calculation
    eq_price = (new_demand_intercept - new_supply_intercept) / (2*slope)
    eq_quantity = new_demand_intercept - slope * eq_price

    st.success(
        f"New Equilibrium → Price = {eq_price:.2f} | Quantity = {eq_quantity:.2f}"
        if lang=="English"
        else f"التوازن الجديد → السعر = {eq_price:.2f} | الكمية = {eq_quantity:.2f}"
    )

    # =====================================
    # Graph
    # =====================================
    prices = np.linspace(0, 100, 100)

    original_demand = base_demand_intercept - slope*prices
    original_supply = base_supply_intercept + slope*prices

    new_demand = new_demand_intercept - slope*prices
    new_supply = new_supply_intercept + slope*prices

    fig = go.Figure()

    # Original curves
    fig.add_trace(go.Scatter(x=prices, y=original_demand, mode='lines', name="Original Demand"))
    fig.add_trace(go.Scatter(x=prices, y=original_supply, mode='lines', name="Original Supply"))

    # Shifted curves
    fig.add_trace(go.Scatter(x=prices, y=new_demand, mode='lines', name="New Demand"))
    fig.add_trace(go.Scatter(x=prices, y=new_supply, mode='lines', name="New Supply"))

    fig.update_layout(
        xaxis_title="Price",
        yaxis_title="Quantity",
        title="Market Shift Simulation" if lang=="English" else "محاكاة تحولات السوق"
    )

    st.plotly_chart(fig, use_container_width=True)
