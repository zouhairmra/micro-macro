import streamlit as st
import numpy as np
import plotly.graph_objects as go


def run(lang="English"):

    # =========================
    # LANGUAGE TEXT
    # =========================

    if lang == "English":

        TITLE = "Demand and Supply Interactive Simulator"
        SCENARIO_LABEL = "Select economic shock"
        EXPLANATION_TITLE = "Economic explanation"
        RESULT_TITLE = "Market result"
        EQUILIBRIUM_TITLE = "Equilibrium"

        SCENARIOS = {

            "No shock": {
                "demand": 0,
                "supply": 0,
                "explanation": "Market is in initial equilibrium"
            },

            "Demand increase (income rise)": {
                "demand": 4,
                "supply": 0,
                "explanation": "Higher income increases demand → Demand shifts RIGHT"
            },

            "Demand decrease (pandemic)": {
                "demand": -5,
                "supply": 0,
                "explanation": "Pandemic reduces consumption → Demand shifts LEFT"
            },

            "Supply increase (technology)": {
                "demand": 0,
                "supply": 4,
                "explanation": "Technology reduces cost → Supply shifts RIGHT (DOWN)"
            },

            "Supply decrease (war)": {
                "demand": 0,
                "supply": -4,
                "explanation": "War increases cost → Supply shifts LEFT (UP)"
            },

            "Supply increase (subsidy)": {
                "demand": 0,
                "supply": 3,
                "explanation": "Subsidy reduces cost → Supply shifts RIGHT"
            },

            "Supply decrease (tax)": {
                "demand": 0,
                "supply": -3,
                "explanation": "Tax increases cost → Supply shifts LEFT"
            }

        }

        PRICE_UP = "Price increases"
        PRICE_DOWN = "Price decreases"

        Q_UP = "Quantity increases"
        Q_DOWN = "Quantity decreases"


    else:

        TITLE = "محاكي العرض والطلب التفاعلي"
        SCENARIO_LABEL = "اختر الصدمة الاقتصادية"
        EXPLANATION_TITLE = "التفسير الاقتصادي"
        RESULT_TITLE = "نتيجة السوق"
        EQUILIBRIUM_TITLE = "التوازن"

        SCENARIOS = {

            "لا توجد صدمة": {
                "demand": 0,
                "supply": 0,
                "explanation": "السوق في حالة توازن أولي"
            },

            "زيادة الطلب (ارتفاع الدخل)": {
                "demand": 4,
                "supply": 0,
                "explanation": "ارتفاع الدخل يزيد الطلب → انتقال منحنى الطلب إلى اليمين"
            },

            "انخفاض الطلب (جائحة)": {
                "demand": -5,
                "supply": 0,
                "explanation": "الجائحة تقلل الاستهلاك → انتقال منحنى الطلب إلى اليسار"
            },

            "زيادة العرض (تكنولوجيا)": {
                "demand": 0,
                "supply": 4,
                "explanation": "التكنولوجيا تقلل التكلفة → انتقال منحنى العرض إلى اليمين (إلى الأسفل)"
            },

            "انخفاض العرض (حرب)": {
                "demand": 0,
                "supply": -4,
                "explanation": "الحرب تزيد التكلفة → انتقال منحنى العرض إلى اليسار (إلى الأعلى)"
            },

            "زيادة العرض (دعم حكومي)": {
                "demand": 0,
                "supply": 3,
                "explanation": "الدعم يقلل التكلفة → انتقال منحنى العرض إلى اليمين"
            },

            "انخفاض العرض (ضريبة)": {
                "demand": 0,
                "supply": -3,
                "explanation": "الضريبة تزيد التكلفة → انتقال منحنى العرض إلى اليسار"
            }

        }

        PRICE_UP = "السعر يرتفع"
        PRICE_DOWN = "السعر ينخفض"

        Q_UP = "الكمية ترتفع"
        Q_DOWN = "الكمية تنخفض"

    # =========================
    # UI
    # =========================

    st.title(TITLE)

    scenario_name = st.selectbox(
        SCENARIO_LABEL,
        list(SCENARIOS.keys())
    )

    demand_shift = SCENARIOS[scenario_name]["demand"]
    supply_shift = SCENARIOS[scenario_name]["supply"]

    explanation = SCENARIOS[scenario_name]["explanation"]

    # =========================
    # BASE CURVES
    # =========================

    P = np.linspace(0, 20, 200)

    a = 16
    b = 0.6
    c = 2
    d = 0.5

    Qd = a - b * P
    Qs = c + d * P

    Qd_new = (a + demand_shift) - b * P
    Qs_new = (c + supply_shift) + d * P

    # =========================
    # EQUILIBRIUM FUNCTION
    # =========================

    def equilibrium(a, b, c, d):

        Pe = (a - c) / (b + d)
        Qe = a - b * Pe

        return Pe, Qe

    Pe, Qe = equilibrium(a, b, c, d)

    Pe_new, Qe_new = equilibrium(
        a + demand_shift,
        b,
        c + supply_shift,
        d
    )

    # =========================
    # GRAPH
    # =========================

    fig = go.Figure()

    fig.add_trace(go.Scatter(x=Qd, y=P, name="Demand"))
    fig.add_trace(go.Scatter(x=Qs, y=P, name="Supply"))

    if demand_shift != 0:
        fig.add_trace(go.Scatter(
            x=Qd_new, y=P,
            name="New Demand",
            line=dict(dash="dash")
        ))

    if supply_shift != 0:
        fig.add_trace(go.Scatter(
            x=Qs_new, y=P,
            name="New Supply",
            line=dict(dash="dash")
        ))

    fig.add_trace(go.Scatter(
        x=[Qe], y=[Pe],
        mode="markers",
        name="Original Equilibrium"
    ))

    fig.add_trace(go.Scatter(
        x=[Qe_new], y=[Pe_new],
        mode="markers",
        name="New Equilibrium"
    ))

    fig.update_layout(
        xaxis_title="Quantity",
        yaxis_title="Price"
    )

    st.plotly_chart(fig, use_container_width=True)

    # =========================
    # EQUILIBRIUM DISPLAY
    # =========================

    st.subheader(EQUILIBRIUM_TITLE)

    col1, col2 = st.columns(2)

    col1.metric("Original Price", round(Pe, 2))
    col1.metric("Original Quantity", round(Qe, 2))

    col2.metric("New Price", round(Pe_new, 2))
    col2.metric("New Quantity", round(Qe_new, 2))

    # =========================
    # EXPLANATION
    # =========================

    st.subheader(EXPLANATION_TITLE)
    st.info(explanation)

    # =========================
    # RESULT
    # =========================

    st.subheader(RESULT_TITLE)

    price_result = PRICE_UP if Pe_new > Pe else PRICE_DOWN
    quantity_result = Q_UP if Qe_new > Qe else Q_DOWN

    st.success(f"{price_result} ، {quantity_result}")
