import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="AgroFly Solutions Dashboard", page_icon="🚁", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for a vibrant and modern UI
st.markdown("""
<style>
    .main {
    }

    .title-text {
        color: #1a5276;
        text-align: center;
        font-weight: 800;
        margin-bottom: 2rem;
    }
    .section-title {
        color: #2980b9;
        font-weight: bold;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #2980b9;
        display: inline-block;
        padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title-text'>🚁 AgroFly Solutions Pvt. Ltd.<br><span style='font-size: 24px; color: #7f8c8d;'>Agricultural Spraying Drone Analysis Dashboard</span></h1>", unsafe_allow_html=True)

# Generate synthetic farm data (from notebook)
@st.cache_data
def generate_synthetic_data():
    np.random.seed(42)
    n = 200
    data = pd.DataFrame({
        "Crop_Type": np.random.choice(["Wheat", "Rice", "Cotton", "Soybean", "Corn", "Sugarcane", "Mustard", "Barley"], n),
        "Field_Size_Acres": np.random.randint(1, 10, n),
        "Crop_Health_Index": np.random.uniform(0.5, 1.0, n),
        "Pesticide_Usage_Liters": np.random.uniform(2, 8, n),
        "Drone_Flight_Time_Minutes": np.random.randint(5, 20, n),
        "Spraying_Efficiency": np.random.uniform(80, 98, n)
    })
    return data

data = generate_synthetic_data()

# Try to load financial data
@st.cache_data
def load_financial_data():
    try:
        # User needs openpyxl to read excel files
        fin_data = pd.read_excel("Agricultural Spraying Drone Financial Analysis.xlsx")
        return fin_data
    except Exception as e:
        return None

fin_data = load_financial_data()

# ----------------- SIDEBAR -----------------
st.sidebar.markdown("## ⚙️ Filter Dashboard Data")

selected_crops = st.sidebar.multiselect(
    "Select Crop Types",
    options=list(data["Crop_Type"].unique()),
    default=list(data["Crop_Type"].unique())
)

min_efficiency, max_efficiency = st.sidebar.slider(
    "Spraying Efficiency Range (%)",
    int(data["Spraying_Efficiency"].min()), int(data["Spraying_Efficiency"].max()) + 1,
    (80, 100)
)

filtered_data = data[
    (data["Crop_Type"].isin(selected_crops)) &
    (data["Spraying_Efficiency"] >= min_efficiency) &
    (data["Spraying_Efficiency"] <= max_efficiency)
]

st.sidebar.markdown("---")
st.sidebar.markdown("**Insights Source:**")
st.sidebar.info("✔ Synthetic Farm Data\\n✔ Financial Analysis Excel")

# ----------------- MAIN LAYOUT -----------------
st.markdown("<h3 class='section-title'>📊 Key Performance Indicators</h3>", unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

avg_pesticide = filtered_data["Pesticide_Usage_Liters"].mean() if not filtered_data.empty else 0
avg_efficiency = filtered_data["Spraying_Efficiency"].mean() if not filtered_data.empty else 0
avg_field = filtered_data["Field_Size_Acres"].mean() if not filtered_data.empty else 0

col1.metric("🚜 Total Fields Analyzed", len(filtered_data))
col2.metric("🎯 Avg Spraying Efficiency", f"{avg_efficiency:.1f}%")
col3.metric("💧 Avg Pesticide Usage", f"{avg_pesticide:.1f} L")
col4.metric("📈 Avg Field Size", f"{avg_field:.1f} Acres")

st.markdown("<h3 class='section-title'>🌱 Technical Data Visualizations</h3>", unsafe_allow_html=True)

if filtered_data.empty:
    st.warning("No data matches the selected filters. Please adjust your selection.")
else:
    col_chart1, col_chart2 = st.columns(2)
    sns.set_theme(style="whitegrid")

    with col_chart1:
        st.markdown("**Crop Type Distribution**")
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        sns.countplot(x="Crop_Type", data=filtered_data, ax=ax1, palette="viridis", order=filtered_data['Crop_Type'].value_counts().index)
        ax1.set_xlabel("Crop Type", fontweight='bold')
        ax1.set_ylabel("Number of Fields", fontweight='bold')
        sns.despine()
        st.pyplot(fig1)

    with col_chart2:
        st.markdown("**Spraying Efficiency Distribution**")
        fig2, ax2 = plt.subplots(figsize=(6, 4))
        sns.histplot(filtered_data["Spraying_Efficiency"], bins=10, kde=True, ax=ax2, color="#3498db")
        ax2.set_xlabel("Efficiency (%)", fontweight='bold')
        ax2.set_ylabel("Frequency", fontweight='bold')
        sns.despine()
        st.pyplot(fig2)

    col_chart3, col_chart4 = st.columns(2)

    with col_chart3:
        st.markdown("**Field Size vs Pesticide Usage**")
        fig3, ax3 = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x="Field_Size_Acres", y="Pesticide_Usage_Liters", hue="Crop_Type", data=filtered_data, ax=ax3, palette="Set2", s=80, alpha=0.8)
        ax3.set_xlabel("Field Size (Acres)", fontweight='bold')
        ax3.set_ylabel("Pesticide Usage (Liters)", fontweight='bold')
        sns.despine()
        st.pyplot(fig3)

    with col_chart4:
        st.markdown("**Crop Health vs Spraying Efficiency**")
        fig4, ax4 = plt.subplots(figsize=(6, 4))
        sns.scatterplot(x="Crop_Health_Index", y="Spraying_Efficiency", hue="Crop_Type", size="Drone_Flight_Time_Minutes", sizes=(20, 200), data=filtered_data, ax=ax4, palette="magma", alpha=0.7)
        ax4.set_xlabel("Crop Health Index", fontweight='bold')
        ax4.set_ylabel("Spraying Efficiency (%)", fontweight='bold')
        # Fix the legend location for better visibility
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
        sns.despine()
        st.pyplot(fig4)

st.markdown("<h3 class='section-title'>💰 Financial Analysis & Conclusions</h3>", unsafe_allow_html=True)

if fin_data is not None:
    st.success("✅ Financial Analysis Data Loaded Successfully")
    st.dataframe(fin_data, use_container_width=True)
else:
    st.info("💡 Tip: To view the full Excel data, please ensure you have 'openpyxl' installed (`pip install openpyxl`). Showing derived conclusions below.")

# The conclusion textual info from the notebook
with st.expander("📌 View Project Conclusions & Recommendations", expanded=True):
    st.markdown("""
    **Conclusion**

    Based on financial and technical analysis, AgroFly Solutions should invest in AI-enabled agricultural drones.

    - 🚀 **Cost Reduction**: The drones reduce operational costs by **35%**, saving approximately **₹31.5 lakhs** per year.
    - ⏳ **ROI / Payback Period**: The investment of **₹60 lakhs** can be recovered in about **1.9 years**.
    - 🌾 **Technical Efficiency**: Drone technology improves spraying efficiency (avg ~89%) and farmer satisfaction, making it a financially and técnically feasible solution.
    - 🎯 **Variables**: Collecting agricultural variables (Crop Type, Field Size, Crop Health Index) and drone variables (Flight Time, Spraying Efficiency, GPS) allows optimized pesticide spraying, reducing chemical waste.
    """)

st.markdown("---")
st.markdown("<center><p style='color: gray; font-size: small;'>Created for AgroFly Solutions Pvt. Ltd. | Analysis Pipeline</p></center>", unsafe_allow_html=True)
