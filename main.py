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

st.write("# This is a H1 header!...") # same as st.title("This is a H1 header!...")
st.write("## This is a H2 header!...")
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
# col2.write(data['title'].unique())
col3.write(data['title'])


# import inspect; print(inspect.signature(col1.metric)) # shall be printed in the console per page refresh (F5)


# file manipulation from perplexity:



st.write("### File Upload Example")

# Add a file uploader button
uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "xlsx"]) # allowed file types as listed

if uploaded_file is not None:
    st.write("File name:", uploaded_file.name)
    # Process the file based on its type
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write(df)
    elif uploaded_file.type == "text/plain":
        text = uploaded_file.read().decode("utf-8")
        st.text_area("File contents", text)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        st.write(df)


import inspect; print(inspect.signature(st.download_button)) # shall be printed in the console per page refresh (F5)
