import streamlit as st
import pandas as pd

st.header("Welcome to Dashboard")
st.subheader("Bar Chart")
data = pd.read_excel("emp.xlsx")
st.bar_chart(data)
