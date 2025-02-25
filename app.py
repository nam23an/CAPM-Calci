import streamlit as st
import matplotlib.pyplot as plt

# Streamlit App Title
st.set_page_config(page_title="CAPM Calculator", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>CAPM Calculator 📊</h1>", unsafe_allow_html=True)

# Sidebar for Inputs
st.sidebar.header("📌 Enter Inputs")
rf = st.sidebar.slider("Risk-Free Rate (R_f) %", 0.0, 20.0, 5.0, 0.1) / 100
beta = st.sidebar.slider("Beta (β)", -2.0, 3.0, 1.0, 0.1)
rm = st.sidebar.slider("Market Return (R_m) %", 0.0, 20.0, 10.0, 0.1) / 100

# CAPM Calculation
def calculate_capm(rf, beta, rm):
    return rf + beta * (rm - rf)

expected_return = calculate_capm(rf, beta, rm)

# Display Results
st.markdown("<h3 style='text-align: center;'>📌 Expected Return: </h3>", unsafe_allow_html=True)
st.markdown(f"<h2 style='text-align: center; color: #FF5733;'>{expected_return:.2%}</h2>", unsafe_allow_html=True)

# Plot Comparison Graph
fig, ax = plt.subplots()
categories = ["Risk-Free Rate", "Expected Return", "Market Return"]
values = [rf, expected_return, rm]
colors = ["blue", "green", "red"]

ax.bar(categories, values, color=colors)
ax.set_ylabel("Return (%)")
ax.set_title("Comparison of Risk-Free, Expected, and Market Return")
st.pyplot(fig)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Designed with ❤️ using Streamlit</p>", unsafe_allow_html=True)
