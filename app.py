import streamlit as st
from PIL import Image
import tempfile

import model

st.title("YOLO Demo")
st.header("This YOLO v3 demo recognizes objects in images and videos.")

st.sidebar.markdown("This demo was made during the Inspirit AI course by [Hugo Dominguez](https://github.com/Clan328).")

uploaded_file = st.file_uploader("Drag and drop any image or video to test the YOLO model", type=["jpg", "jpeg", "png", "mp4", "mov"])

if uploaded_file is not None:
  if uploaded_file.type.startswith("image"):
    image = Image.open(uploaded_file)
    st.image(model.detect_image(image))
  else:
    tfile = tempfile.NamedTemporaryFile(delete=False) 
    tfile.write(uploaded_file.read())

    path = tempfile.NamedTemporaryFile(suffix='.mkv', delete=False)

    model.detect_video(tfile.name, path.name)

    progress = st.empty()
    progress.empty()

    st.video(path.name)