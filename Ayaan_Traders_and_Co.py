import streamlit as st

# Set page configuration
st.set_page_config(page_title="Ayaan Traders & Co.", layout="wide", initial_sidebar_state="expanded")

# Display the logo and title in the header
col1, col2, col3 = st.columns([1, 1, 4])

with col1:
    st.image("data/logo.jpg", width=150)

with col3:
    st.title("Ayaan Traders & Co."
             "\nEnterprise Tile Management App")

# Sidebar Navigation with an additional "About" page
st.sidebar.title("Navigation")
pages = ["Pricing and Cost Estimation", "Measuring and Billing",
         "Labor Management", "Tools for Management", "Compliance and Insurance", "About Us"]

selected_page = st.sidebar.selectbox("Select a page", pages)

# Import and render the correct page based on selection
if selected_page == "Pricing and Cost Estimation":
    import pages.Pricing_and_Cost_Estimation
elif selected_page == "Measuring and Billing":
    import pages.Measuring_and_Billing
elif selected_page == "Labor Management":
    import pages.Labor_Management
elif selected_page == "Tools for Management":
    import pages.Tools_Management
elif selected_page == "Compliance and Insurance":
    import pages.Compliance_and_Insurance

st.write("""
**Ayaan Traders & Co.** is a leading enterprise in the construction industry, specializing in tile fixing solutions.
With over 20 years of experience in delivering high-quality tile installation services, we focus on bringing precision,
craftsmanship, and efficiency to every project. Our team of expert laborers ensures the best outcomes, whether for
residential or commercial projects.
""")
st.subheader("Mission")
st.write("""
Our mission is to provide the highest quality tile fixing services while ensuring that projects are completed
efficiently and within budget. We pride ourselves on maintaining exceptional customer satisfaction.
""")
st.subheader("Contact Us")
st.write("""
For inquiries, please contact us:

- **Phone**: +123-456-7890
- **Email**: support@ayaantraders.com
- **Website**: [www.ayaantraders.com](http://www.ayaantraders.com)
""")

# Footer with Copyright Information
st.markdown(
    """
    <style>
    footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        color: gray;
        text-align: justified;
        padding: 10px;
        background-color: #f9f9f9;
    }
    .footer-text {
        font-size: 0.8em;
    }
    </style>
    <footer>
        <div class="footer-text">
            © 2024 Ayaan Traders & Co. All Rights Reserved. | Designed by Ayaan Traders IT Department
        </div>
    </footer>
    """,
    unsafe_allow_html=True
)
