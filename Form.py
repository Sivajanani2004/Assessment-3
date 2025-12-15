import streamlit as st
if st.form("Form"):
    name = st.text_input("Enter your name")
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age",step=1)
    submit = st.button("Submit")
    if submit:
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Age: {age}")
        
if submit and not email:
    st.error("Email is invalid")
if submit and email:
    st.success("Login Sucessfully")