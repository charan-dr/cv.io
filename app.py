import cv2
import streamlit as st
import mediapipe as mp
import numpy as np
from PIL import Image

# --- MediaPipe Selfie Segmentation Setup ---
mp_selfie_segmentation = mp.solutions.selfie_segmentation
selfie_segmentation = mp_selfie_segmentation.SelfieSegmentation(model_selection=0)  # 0 = general model

# --- Streamlit App UI ---
st.set_page_config(page_title="AI Background Remover", layout="wide")
st.title("🎥 Real-Time AI Background Replacement & Blur")
st.sidebar.header("Controls")

# --- Sidebar Controls ---
run = st.sidebar.checkbox('Start Webcam', value=True)
effect = st.sidebar.radio("Select Effect", ('Replace Background', 'Blur Background'))
if effect == 'Blur Background':
    blur_amount = st.sidebar.slider("Blur Intensity", 1, 49, 15, step=2)
else:
    blur_amount = 0

uploaded_file = st.sidebar.file_uploader("Upload Background Image", type=['jpg', 'jpeg', 'png'])

# --- Load Background Image ---
if uploaded_file is not None:
    background_image = np.array(Image.open(uploaded_file))
    if background_image.shape[2] == 4:  # Convert RGBA to RGB if needed
        background_image = cv2.cvtColor(background_image, cv2.COLOR_RGBA2RGB)
else:
    background_image = np.zeros((480, 640, 3), np.uint8)
    background_image[:] = (0, 200, 0)  # Default green background

FRAME_WINDOW = st.image([])
cap = cv2.VideoCapture(0)

# --- Main Loop ---
while run:
    ret, frame = cap.read()
    if not ret:
        st.error("Failed to access webcam.")
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # --- Get segmentation mask ---
    results = selfie_segmentation.process(frame_rgb)
    mask = results.segmentation_mask

    # --- Thresholding to separate foreground and background ---
    condition = np.stack((mask,) * 3, axis=-1) > 0.4

    # --- Resize background to match frame ---
    bg_resized = cv2.resize(background_image, (frame.shape[1], frame.shape[0]))

    if effect == 'Replace Background':
        output_image = np.where(condition, frame, bg_resized)
    else:
        blurred_frame = cv2.GaussianBlur(frame, (blur_amount, blur_amount), 0)
        output_image = np.where(condition, frame, blurred_frame)

    FRAME_WINDOW.image(output_image, channels='BGR')

else:
    st.write("Webcam is off.")
    cap.release()
