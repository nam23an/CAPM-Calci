import streamlit as st
import numpy as np
import pandas as pd
# Set page configuration
st.set_page_config(page_title="CAPM Calculator", page_icon="📊", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stApp { background-color: #f7f7f7; }
    .main { background-color: white; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px gray; }
    .stTextInput, .stNumberInput { border-radius: 5px !important; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with title
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Modern_Portfolio_Theory.png", use_container_width=True)
st.sidebar.title("📈 CAPM Calculator")
st.sidebar.markdown("This tool helps you calculate the *Expected Return* using the Capital Asset Pricing Model (CAPM).")

# Main content
st.markdown('<div class="main">', unsafe_allow_html=True)
st.title("📊 Capital Asset Pricing Model (CAPM) Calculator")

# User Inputs
st.write("### 🔢 Enter the following values:")

col1, col2, col3 = st.columns(3)

with col1:
    rf = st.number_input("Risk-Free Rate (rf) in %", value=2.0, step=0.1)

with col2:
    beta = st.number_input("Beta (β)", value=1.0, step=0.1)

with col3:
    rm = st.number_input("Market Return (rm) in %", value=8.0, step=0.1)

# CAPM Calculation Function
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

# Calculate Button
if st.button("📌 Calculate CAPM"):
    with st.spinner("Calculating... ⏳"):
        result = calculate_capm(rf, beta, rm)
        st.success(f"📊 CAPM Expected Return: *{result:.2f}%*")

    # Visualization
    st.write("### 📈 CAPM Formula Visualization")
    fig, ax = plt.subplots(figsize=(6, 3))
    x = np.linspace(0, 2, 10)  # Simulated beta values
    y = rf + x * (rm - rf)  # Expected return

    ax.plot(x, y, label="Expected Return", color="blue", linewidth=2)
    ax.scatter(beta, result, color="red", s=100, label="Your Input")
    ax.set_xlabel("Beta (β)")
    ax.set_ylabel("Expected Return (%)")
    ax.legend()
    ax.grid()

    st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)
