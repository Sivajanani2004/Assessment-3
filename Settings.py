import streamlit as st
st.subheader("Settings Page")
tab1,tab2 = st.tabs(["About","Advanced Settings"])
with tab1:
    st.markdown("About page")
with tab2:
    st.markdown("Advanced setting tab page")

