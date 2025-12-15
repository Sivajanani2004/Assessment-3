import streamlit as st

st.subheader("Calculator")
op = st.selectbox("Select Operation",["Add","Sub","Mul","Div"])
num1 = st.number_input("Enter num1",step=1)
num2 = st.number_input("Enter num2",step=1)
add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
if st.button("Click"):
    if op == "Add":
        st.write(f"Addition: {add}")
    elif op == "Sub":
        st.write(f"Subtraction: {sub}")
    elif op == "Mul":
        st.write(f"Multiplication: {mul}")
    elif op == "Div":
     try:
        st.write(f"Division: {div}")
     except ZeroDivisionError:
        st.write("Do not divide by zero")