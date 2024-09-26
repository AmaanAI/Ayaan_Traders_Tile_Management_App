import streamlit as st
import pandas as pd

st.title("Pricing and Cost Estimation")

# Load and edit pricing information
tile_rates = pd.read_csv("data/tile_rates.csv")

st.subheader("Tile Fixing Rates")
st.dataframe(tile_rates)

# Update pricing
if st.button("Update Rates"):
    # Logic for updating rates
    st.success("Tile rates updated successfully!")

# Cost Estimation Form
st.subheader("Cost Estimation")

sq_ft_area = st.number_input("Enter the area (sq. ft.)", min_value=0.0)

# Tile rate selection (Ensure rate is converted to a float)
tile_rate = st.selectbox("Select tile type", tile_rates['Tile Type'])
selected_rate = float(tile_rates[tile_rates['Tile Type'] == tile_rate]['Rate per sq ft'].values[0])

# Material cost input
material_cost_per_sqft = st.number_input("Material cost per sq. ft.", min_value=0.0)

markup = st.slider("Select markup percentage", min_value=0, max_value=50)

# Ensure the values are treated as floats for calculation
total_cost = (sq_ft_area * (selected_rate + material_cost_per_sqft)) * (1 + markup / 100)
st.write(f"**Total Estimated Cost:** ${total_cost:.2f}")
