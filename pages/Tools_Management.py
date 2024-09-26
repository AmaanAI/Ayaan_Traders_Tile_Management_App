import streamlit as st

st.title("Tools for Management")

st.subheader("Tracking Tools and Equipment")
tools = st.text_area("Enter tools used (e.g., trowels, spacers, etc.)")

if st.button("Add Tools"):
    st.success("Tools added to the project.")

# Labor Cost Calculator
st.subheader("Labor Cost Calculator")

sq_ft_area = st.number_input("Enter area in sq. ft.", min_value=0.0)
labor_rate_per_sq_ft = st.number_input("Labor rate per sq. ft.", min_value=0.0)

total_labor_cost = sq_ft_area * labor_rate_per_sq_ft
st.write(f"**Total Labor Cost:** ${total_labor_cost:.2f}")
