import streamlit as st

st.write("# Scheme Page")

from PIL import Image
image = Image.open("./Input/basic_image.png")
st.image(image, caption='UDP tralala...', use_container_width=True)
