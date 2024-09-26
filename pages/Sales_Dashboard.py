import streamlit as st
import streamlit.components.v1 as components

# Set up the page
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Define the page header
st.markdown("<h1 style='text-align: center;'>Ayaan Traders & Co. Sales Dashboard</h1>", unsafe_allow_html=True)

# Layout - Using columns for different sections
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

# Key Performance Indicators (KPIs)
with kpi_col1:
    st.metric(label="Total Sales", value="4,785", delta="+15%")
with kpi_col2:
    st.metric(label="Market Share", value="26%", delta="+5%")
with kpi_col3:
    st.metric(label="Revenue Growth", value="55%", delta="-3%")

# Chart.js Integration: Monthly Sales
st.markdown("### Monthly Sales")
monthly_sales_chart = """
<canvas id="monthlySalesChart" width="400" height="200"></canvas>
<script>
var ctx = document.getElementById('monthlySalesChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Monthly Sales',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            data: [1200, 1900, 3000, 5000, 2300, 2500, 3200, 4200, 3800, 4600, 5400, 6000]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false }
        },
        scales: {
            x: { beginAtZero: true },
            y: { beginAtZero: true }
        }
    }
});
</script>
"""
components.html(monthly_sales_chart, height=300)

# Chart.js Integration: Sales by Region
st.markdown("### Sales by Region")
sales_by_region_chart = """
<canvas id="salesByRegionChart" width="400" height="200"></canvas>
<script>
var ctx = document.getElementById('salesByRegionChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['North', 'South', 'East', 'West'],
        datasets: [{
            label: 'Sales by Region',
            backgroundColor: ['#36a2eb', '#ff6384', '#4bc0c0', '#ffce56'],
            data: [5000, 7000, 4000, 8000]
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: { beginAtZero: true },
            y: { beginAtZero: true }
        }
    }
});
</script>
"""
components.html(sales_by_region_chart, height=300)

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
