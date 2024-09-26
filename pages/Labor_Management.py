import streamlit as st
import pandas as pd

st.title("Labor Management")

# Laborer Info
labor_info = pd.read_csv("data/laborer_info.csv")
st.subheader("Laborers")
st.dataframe(labor_info)

# Scheduling
st.subheader("Laborer Scheduling")
labor_name = st.selectbox("Select Laborer", labor_info['Name'])
date = st.date_input("Select date")
hours_worked = st.number_input("Hours Worked", min_value=0.0)

if st.button("Add Schedule"):
    st.success(f"Schedule added for {labor_name} on {date} for {hours_worked} hours.")

# Incentive Management
st.subheader("Incentive Management")
completion_rate = st.slider("Completion Rate (%)", 0, 100)
if completion_rate > 90:
    st.write(f"**Bonus Eligible!** Consider offering a bonus to laborers.")
