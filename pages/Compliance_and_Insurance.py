import streamlit as st

st.title("Compliance and Insurance")

st.subheader("Worker Insurance")
insurance_info = st.text_input("Enter worker insurance details")

if st.button("Save Insurance Info"):
    st.success("Insurance details saved.")

st.subheader("Permits and Licensing")
permit_info = st.text_input("Enter required permits")

if st.button("Save Permit Info"):
    st.success("Permit details saved.")
