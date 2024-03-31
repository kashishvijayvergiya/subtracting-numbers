import streamlit as st

def subtract(a,b):
  return(a-b)

st.title("Calc")
a = st.number_input("Input your first number : ")
b = st.number_input("Input your second number : ")

answer = subtract(a,b)
st.write(answer)
