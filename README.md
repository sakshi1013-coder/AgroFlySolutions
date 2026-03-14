# 🚁 AgroFly Solutions: Agricultural Spraying Drone Analysis

This repository contains a comprehensive data analysis and interactive dashboard for the **AgroFly Solutions Pvt. Ltd.** case study. The project evaluates the financial, technical, and CRM impact of transitioning from manual pesticide spraying to AI-enabled agricultural drones.

## 🌟 Features

- **Interactive Streamlit Dashboard (`app.py`)**: A modern, vibrant web application that visualizes the theoretical impact of drone adoption across simulated farms.
- **Parametric Data Filtering**: Users can filter by crop types (Wheat, Rice, Cotton, Soybean, Corn, Sugarcane, Mustard, Barley) and spray efficiency metrics.
- **Synthetic Data Generation**: Simulates 200 real-world farm conditions (field size, crop health, drone flight time) using Python (`numpy` and `pandas`).
- **Data Visualizations**: Includes analytical charts built with `seaborn` and `matplotlib` to explore pesticide usage vs. field size and crop health vs. spraying efficiency.
- **Financial Analysis Insight**: Highlights projected cost reduction (35%), expected annual savings (₹31.5 Lakhs), and Return on Investment (1.9 years payback period).

## 🛠️ Technologies Used

- **Python 3**
- **Streamlit** (for the interactive UI)
- **Pandas** (for data manipulation and reading financial sheets)
- **NumPy** (for synthetic data generation)
- **Matplotlib & Seaborn** (for data visualization)
- **Jupyter Notebook** (Initial analysis sandbox)

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sakshi1013-coder/AgroFlySolutions.git
   cd AgroFlySolutions
   ```

2. **Install the required dependencies:**
   Ensure you have Python installed, then run:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn openpyxl
   ```
   *(Note: `openpyxl` is required to read the Financial Analysis Excel file.)*

3. **Run the Dashboard:**
   Start the Streamlit development server:
   ```bash
   streamlit run app.py
   ```

4. **View the App:**
   Open your browser and navigate to `http://localhost:8501`.

## 📁 Project Structure

- `app.py`: The main Streamlit dashboard application containing the UI, synthetic data logic, and visualizations.
- `Agricultural_Spraying_Drone_Analysis.ipynb`: The original Jupyter Notebook containing the foundational logic and algorithms.
- `Agricultural Spraying Drone Financial Analysis.xlsx`: The raw financial data evaluated to approve drone investments.

## 📊 Case Study Overview

**AgroFly Solutions** currently relies on slow, labor-intensive manual pesticide spraying. By investing ₹60 Lakhs in AI-enabled agricultural drones, the company aims to:
1. **Reduce Operational Costs**: Save ₹31.5 Lakhs annually.
2. **Improve Spraying Efficiency**: Achieve ~90% efficiency, minimizing chemical waste.
3. **Enhance Customer Retention**: Stop the 10-15% crop productivity loss caused by manual spraying delays, thereby boosting farmer profitability and satisfaction.
