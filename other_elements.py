# YT URL: https://www.youtube.com/watch?v=_Um12_OlGgw&t=476s

import streamlit as st
import time

if "photo" not in st.session_state: # managing flags
    st.session_state["photo"] = "not done"

col1, col2, col3 = st.columns([1, 2, 1]) # 1:2:1 ratio for column widths

col1.markdown("### Welcome to my app!")
col1.markdown("Here is some info on the app. ")


def change_photo_state():
    st.session_state["photo"] = "done"

uploaded_photo = col2.file_uploader("Upload a photo", type=["jpg", "png", "jpeg"], on_change=change_photo_state)
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

if st.session_state["photo"] == "done":

    progress_bar = col2.progress(0)

    for perc_completed in range(100):
        time.sleep(0.05)
        progress_bar.progress(perc_completed + 1)


    col2.success("Photo uploaded succefully!")
    # if uploaded_photo is not None:
    #     col2.image(uploaded_photo, caption="Uploaded Photo", use_column_width=True)

    col3.metric(label="Temperature", value="60 °C", delta="3 °C")

    with st.expander("click to read more"):
        st.write("Hello, here are more details on this topic that you were interesetd in.")

        if uploaded_photo is None:
            st.image(camera_photo)
        else:
            st.image(uploaded_photo)