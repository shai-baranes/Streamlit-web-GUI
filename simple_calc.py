# from YT URL: https://www.youtube.com/watch?v=D0D4Pa22iG0
# streamlit basic documentation: https://docs.streamlit.io/library/get-started
# streamlit api documentation: https://docs.streamlit.io/library/api-reference

# to run it from cmd line: 'streamlit run simple_clac.py'

import pandas as pd
import streamlit as st


# now create a basic web interactive calculator using streamlit:
st.write("## Simple Calculator")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

st.write("### Choose an operation:")

operation = st.selectbox("Operation", ["Add", "Subtract", "Multiply", "Divide"])
num1 = st.number_input("Enter first number", value=0)
num2 = st.number_input("Enter second number", value=0)

result = ' _'
# result = None

if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    
st.write(f"The result is: {result}")


# Load a sample dataset and display it
st.write("## Sample Dataset")
df = pd.DataFrame({
    'Column 1': [1, 2, 3, 4],
    'Column 2': ['A', 'B', 'C', 'D']
})
st.write(df)

# Display a simple line chart
st.write("## Sample Line Chart")
st.line_chart(df['Column 1'])

# Display a simple bar chart
st.write("## Sample Bar Chart")
st.bar_chart(df['Column 1'])