import streamlit as st
import pandas as pd
data = pd.read_excel("emp.xlsx")
st.subheader("Welcome to Data viewer")
with st.expander("Preview"):
    st.write("Data Viewer")
    st.dataframe(data)
