import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Set up page configuration
st.set_page_config(page_title="Ayaan Traders & Co. Sales Dashboard", layout="wide")

# Title
st.markdown("<h1 style='text-align: center;'>Ayaan Traders & Co. Sales Dashboard</h1>", unsafe_allow_html=True)

# Create sample sales data for demonstration
np.random.seed(42)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
regions = ["North", "South", "East", "West"]
products = ["Product A", "Product B", "Product C", "Product D"]

data = {
    "Month": np.random.choice(months, 100),
    "Region": np.random.choice(regions, 100),
    "Product": np.random.choice(products, 100),
    "Sales": np.random.randint(100, 5000, 100),
    "Revenue": np.random.randint(1000, 10000, 100),
}

df = pd.DataFrame(data)

# KPI Section (use metrics)
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

with kpi_col1:
    st.metric(label="Total Sales", value=f"{df['Sales'].sum():,}")
with kpi_col2:
    st.metric(label="Total Revenue", value=f"${df['Revenue'].sum():,}")
with kpi_col3:
    st.metric(label="Average Sale", value=f"${df['Revenue'].mean():,.2f}")

# Layout for Charts - 10 different charts
chart_col1, chart_col2, chart_col3 = st.columns(3)

# Chart 1: Sales by Month (Bar Chart)
with chart_col1:
    st.markdown("#### Sales by Month")
    sales_by_month = df.groupby("Month").sum().reset_index()
    fig1 = px.bar(sales_by_month, x="Month", y="Sales", title="Sales by Month", color="Sales", text="Sales")
    st.plotly_chart(fig1)

# Chart 2: Revenue by Month (Line Chart)
with chart_col2:
    st.markdown("#### Revenue by Month")
    revenue_by_month = df.groupby("Month").sum().reset_index()
    fig2 = px.line(revenue_by_month, x="Month", y="Revenue", title="Revenue by Month", markers=True)
    st.plotly_chart(fig2)

# Chart 3: Sales by Region (Pie Chart)
with chart_col3:
    st.markdown("#### Sales by Region")
    sales_by_region = df.groupby("Region").sum().reset_index()
    fig3 = px.pie(sales_by_region, names="Region", values="Sales", title="Sales by Region")
    st.plotly_chart(fig3)

# Second Row of Charts
chart_col4, chart_col5, chart_col6 = st.columns(3)

# Chart 4: Revenue by Region (Bar Chart)
with chart_col4:
    st.markdown("#### Revenue by Region")
    fig4 = px.bar(sales_by_region, x="Region", y="Revenue", color="Region", title="Revenue by Region", text="Revenue")
    st.plotly_chart(fig4)

# Chart 5: Sales by Product (Horizontal Bar Chart)
with chart_col5:
    st.markdown("#### Sales by Product")
    sales_by_product = df.groupby("Product").sum().reset_index()
    fig5 = px.bar(sales_by_product, x="Sales", y="Product", orientation="h", title="Sales by Product", color="Sales", text="Sales")
    st.plotly_chart(fig5)

# Chart 6: Revenue by Product (Bar Chart)
with chart_col6:
    st.markdown("#### Revenue by Product")
    fig6 = px.bar(sales_by_product, x="Product", y="Revenue", color="Revenue", title="Revenue by Product", text="Revenue")
    st.plotly_chart(fig6)

# Third Row of Charts
chart_col7, chart_col8, chart_col9 = st.columns(3)

# Chart 7: Sales Distribution (Box Plot)
with chart_col7:
    st.markdown("#### Sales Distribution")
    fig7 = px.box(df, x="Product", y="Sales", color="Product", title="Sales Distribution by Product")
    st.plotly_chart(fig7)

# Chart 8: Revenue Distribution (Box Plot)
with chart_col8:
    st.markdown("#### Revenue Distribution")
    fig8 = px.box(df, x="Product", y="Revenue", color="Product", title="Revenue Distribution by Product")
    st.plotly_chart(fig8)

# Chart 9: Correlation between Sales and Revenue (Scatter Plot)
with chart_col9:
    st.markdown("#### Sales vs Revenue")
    fig9 = px.scatter(df, x="Sales", y="Revenue", color="Product", title="Correlation between Sales and Revenue", size="Revenue", hover_name="Product")
    st.plotly_chart(fig9)

# Fourth Row of Charts
chart_col10 = st.columns(1)

# Chart 10: Sales by Region and Product (Treemap)
with chart_col10[0]:
    st.markdown("#### Sales by Region and Product")
    fig10 = px.treemap(df, path=["Region", "Product"], values="Sales", title="Sales by Region and Product", color="Sales")
    st.plotly_chart(fig10)

# Footer
st.markdown(
    """
    <style>
    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        color: gray;
        text-align: center;
        padding: 10px;
        background-color: #f9f9f9;
    }
    </style>
    <footer>
        © 2024 Ayaan Traders & Co. All Rights Reserved.
    </footer>
    """,
    unsafe_allow_html=True
)
