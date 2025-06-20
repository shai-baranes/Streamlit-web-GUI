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

st.write("# This is a H1 header!...")
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


st.video(data = "./Input/test_vid.webm", loop= True, autoplay=True, muted=True, width='stretch')


st.write('### Utilizing Columns')
col1, col2, col3 = st.columns(3)
col1.write("This is the first column.")
col2.write("This is the second column.")
col3.write("This is the third column.")


col1.metric(label="Metric 1", value=123, delta=5, border=True)
col2.metric(label="Metric 2", value=456, delta=-3, border=True)
col3.metric(label="Metric 3", value=789, delta=10, border=True)


col1.write("TBD")
col2.write("All movie titles")
col3.write("Displaying only the 'title' column")
col2.write(np.array(sorted(str(i) for i in data['title'].unique() if type(i) != 'str'))) # each cell can easily accumulate np.array values
# col2.write(sorted([str(i) for i in data['title'].unique().tolist() if type(i) != 'str']))
# col2.write(data['title'].unique())
col3.write(data['title'])

# print(np.sort(data['title'].unique()))
# print(type(data['title'].unique()))

# import inspect; print(inspect.signature(col1.metric)) # shall be printed in the console per page refresh (F5)

# how to sort 'numpy.ndarray'?
# print(sorted(data['title'].unique())) # does not work, since it is a numpy array
# print(data['title'].unique().sort()) # does not work, since it is a numpy array
# print(data['title'].unique().sort()) # does not work, since it is a numpy array
# print(data['title'].unique().sort()) # does not work, since it is a numpy array
# print(np.sort(data['title'].unique())) # does not work, since it is a numpy array
# print(np.sort(data['title'].unique())) # does not work, since it is a numpy array

# print(data['title'].unique().tolist()) # works, since it is a list now
print("shai")

# how to convert numpy array to list?
# print(type(data['title'].unique()))
# print(data['title'].unique().tolist())

# print(sorted(data['title'].unique().tolist())) # works, since it is a list now


# i.tbd  for i in data['title'].unique().tolist() else i

# one liner for if els in list comprehension
# print([i for i in data['title'].unique().tolist() if i != '']) # works, since it is a list now

# print(sorted([str(i) for i in data['title'].unique() if type(i) != 'str'])) # works, since it is a list now
# print(sorted([str(i) for i in data['title'].unique().tolist() if type(i) != 'str'])) # works, since it is a list now


print(type(data['title'].unique()))

# how to convert a list into numpy.ndarray?
# print(np.array(data['title'].unique())) # works, since it is a numpy array now
