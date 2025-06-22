# YT URL:  https://www.youtube.com/watch?v=2siBrMsqF44
# after running -> drag the Sample_Data... csv file to the UI control element (from the 'Input' folder)


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
# import plotly.graph_objs as go

st.set_page_config(page_title="Tech with Tim", page_icon=":robot:", layout="wide")
st.write("# Tech with Tim - Streamlit Tutorial:")


# plotly example
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=[1, 2, 3], y=[1, 4, 9],
    line=dict(width=1)  # Thinner line
))
fig.add_trace(go.Scatter(
    x=[1, 2, 3], y=[9, 4, 1],
    line=dict(width=3, color="red")  # Thinner line
))
fig.update_layout(
    title={'text': '"plotly" Plot', 'font': {'size': 20}},
    xaxis=dict(title='X axis', tickfont=dict(size=20)),
    # xaxis=dict(title='X axis', titlefont=dict(size=10), tickfont=dict(size=8)),
    yaxis=dict(title='Y axis', tickfont=dict(size=20)),
    # yaxis=dict(title='Y axis', titlefont=dict(size=10), tickfont=dict(size=8)),
    font=dict(size=20)  # General font size
)
st.plotly_chart(fig, use_container_width=False)
# st.plotly_chart(fig, use_container_width=True)



uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
# uploaded_file = st.file_uploader("Choose a CSV file", type="csv", label_visibility="collapsed")

if uploaded_file is not None:
    # st.write("File uploaded...")
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")
    st.write(df.head()) # preview of DF

    st.subheader('Data Summary')
    st.write(df.describe())  # summary statistics

    st.subheader("Filter Data")
    columns = df.columns.to_list()
    sorted_columns =  sorted(str(i) for i in columns if type(i) != 'str')
    selected_column = st.selectbox("Select column to filter by", sorted_columns) # TBD sort values as done before
    # selected_column = st.selectbox("Select column to filter by", columns) # TBD sort values as done before
    unique_values = df[selected_column].unique()
    sorted_unique_values = sorted(str(i) for i in unique_values if type(i) != 'str')
    selected_value = st.selectbox("Select value", sorted_unique_values)  # TBD sort values as done before
    # selected_value = st.selectbox("Select value", unique_values)  # TBD sort values as done before

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", sorted_columns)
    y_column = st.selectbox("Select Y-axis column", sorted_columns)


    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(x_column)[y_column])

else:
    st.write("Waiting on file upload...")