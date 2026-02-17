import streamlit as st

def run():

    st.header("📊 مرونة الطلب السعرية")

    st.write("""
    مرونة الطلب = نسبة التغير في الكمية ÷ نسبة التغير في السعر
    """)

    dq = st.number_input("نسبة التغير في الكمية (%)", value=10.0)
    dp = st.number_input("نسبة التغير في السعر (%)", value=5.0)

    if dp != 0:
        elasticity = dq / dp
        st.subheader(f"قيمة المرونة = {round(elasticity,2)}")

        if abs(elasticity) > 1:
            st.success("الطلب مرن")
        elif abs(elasticity) < 1:
            st.warning("الطلب غير مرن")
        else:
            st.info("مرونة وحدية")
