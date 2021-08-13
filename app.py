import streamlit as st
# from PIL import Image
# import tempfile
import os

st.set_page_config(page_title="YOLO Demo", layout="wide")

os.system("sudo reboot")
os.system("less /proc/meminfo")

# if not os.path.exists("data/yolo_weights.h5"):
#     with st.spinner("Loading model..."):
#         os.system("wget --no-check-certificate -O data/yolo_weights.h5 \"https://storage.googleapis.com/inspirit-ai-data-bucket-1/Data/AI%20Scholars/Sessions%206%20-%2010%20(Projects)/Project%20-%20%20Object%20Detection%20(Autonomous%20Vehicles)/yolo.h5\"")
#         from model import detect_image, detect_video
# else:
#     from model import detect_image, detect_video

st.title("YOLO Demo")
st.header("This YOLO v3 demo recognizes objects in images and videos.")

st.sidebar.markdown("This demo was made during the Inspirit AI course by [Hugo Dominguez](https://github.com/Clan328).")

# uploaded_file = st.file_uploader("Drag and drop any image or video to test the YOLO model", type=["jpg", "jpeg", "png", "mp4", "mov"])

# if uploaded_file is not None:
#   if uploaded_file.type.startswith("image"):
#     image = Image.open(uploaded_file)
#     st.image(detect_image(image))
#   else:
#     tfile = tempfile.NamedTemporaryFile(delete=False) 
#     tfile.write(uploaded_file.read())

#     path = tempfile.NamedTemporaryFile(suffix='.mp4', delete=False)

#     detect_video(tfile.name, path.name)

#     progress = st.empty()
#     progress.empty()

#     st.video(path.name)