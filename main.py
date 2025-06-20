# to run it from cmd line: 'streamlit run main.py'

# from YT URL: https://www.youtube.com/watch?v=D0D4Pa22iG0
# streamlit basic documentation: https://docs.streamlit.io/library/get-started
# streamlit api documentation: https://docs.streamlit.io/library/api-reference
# streamlit charts documentation: https://docs.streamlit.io/library/api-reference/charts

# note that after adding pages, weneed to re-execute the script (F5 is not sufficent)
# note also that you probably need to sepreate projects directories since the pages are shared
# note also that after removing data from page, you get to see the changes only after clicking the newly and temporarily introduced button at the top - called: 'rerun'

import pandas as pd
import streamlit as st
import numpy as np

st.write("# This is a H1 header!")
st.write("## This is a H2 header!")
st.write("### This is a H3 header!")

st.write("Hello, world! Shai!!__")

my_text = st.text_input("Enter some text:")

st.write(f"You typed: {my_text}")

is_clicked = st.button("Click me!")

st.write(is_clicked)

# --------------------

data = pd.read_csv("./Input/movies.csv")
st.write("## Movies Dataset")
st.write(data)

st.link_button(label="Tutorial", url="https://www.youtube.com/watch?v=D0D4Pa22iG0", icon="📖")
# st.link_button("https://www.youtube.com/watch?v=D0D4Pa22iG0", "Watch the tutorial on YouTube!")
import inspect; print(inspect.signature(st.link_button))
# label: 'str'
