AI Background Remover
An interactive real-time AI-powered background remover and blur application built with Streamlit, OpenCV, and MediaPipe.
This project uses MediaPipe’s Selfie Segmentation model to detect the person in a webcam feed and allows users to either replace or blur the background dynamically.

Features
AI-based Background Segmentation — Uses MediaPipe Selfie Segmentation for accurate real-time detection.
Real-Time Webcam Processing — Works live from your webcam using Streamlit’s interactive interface.
Background Replacement — Upload any custom image to replace your current background.
Adjustable Blur Effect — Choose the blur intensity for background softening.
User-Friendly UI — Streamlit sidebar controls for easy customization.

Tech Stack
Component	Description
Python	Core programming language
Streamlit	Web app framework for interactivity
OpenCV	Image processing and webcam access
MediaPipe	AI segmentation model for person detection
NumPy	Array operations for image manipulation
Pillow (PIL)	Image loading and format conversion

Installation
1️. Clone this repository
git clone https://github.com/your-username/ai-background-remover.git
cd ai-background-remover

2️. Create and activate a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate  # For Windows
source venv/bin/activate  # For macOS/Linux

3️. Install dependencies
pip install -r requirements.txt

If you don’t have a requirements.txt, use:
pip install streamlit opencv-python mediapipe numpy pillow

Usage
Run the Streamlit app using:
streamlit run app.py
Then open the local URL provided by Streamlit (usually http://localhost:8501
).

How It Works
Capture webcam feed using OpenCV.
Convert the frame to RGB and pass it to MediaPipe’s Selfie Segmentation model.
Generate a binary mask separating the person (foreground) from the background.

Depending on user choice:
Replace the background with a custom uploaded image, or
Apply Gaussian Blur to the background.
Display the processed frame in real time within the Streamlit interface.

Controls
Control	Description
Start Webcam	Toggles webcam feed on/off
Select Effect	Choose between background replacement or blur
Blur Intensity	Adjust the strength of blur (1–49)
Upload Background Image	Upload any .jpg, .jpeg, or .png image to use as a custom background

Example
Mode	Description
Replace Background	Shows user with a new uploaded image as background
Blur Background	Keeps the person clear and blurs everything else

License
This project is licensed under the MIT License — you’re free to use, modify, and distribute it.

Future Improvements
Add image background filters (e.g., grayscale, artistic effects)
Include option to capture and save snapshots
Add multi-person segmentation support
Optimize for lower latency on slower systems
