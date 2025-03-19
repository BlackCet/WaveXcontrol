# AI-Gesture Mouse Control

Traditional input devices such as a mouse and keyboard can be restrictive for users with mobility impairments and may not always provide the most efficient or intuitive way to interact with a computer. Gesture-based interaction offers a hands-free alternative that enhances accessibility and user experience. This project proposes an AI-powered virtual mouse using computer vision and deep learning to recognize hand gestures for controlling cursor movement and performing essential mouse functions like clicking and scrolling.

## Features
- Hand Gesture Recognition – Detects and interprets hand gestures to control the mouse.
- Real-Time Performance – Optimized for low latency and smooth interaction.
- Accurate and Robust – Trained on diverse datasets to handle various lighting conditions, hand sizes, and backgrounds.
- Enhanced User Interaction – Ensures a seamless experience with intuitive gestures.
- Optimized Model – Uses ONNX for efficient inference.

## Technology Stack
- Programming Language: Python
- Libraries: OpenCV, MediaPipe, TensorFlow/PyTorch, pyautogui
- Deployment: Streamlit (UI), ONNX (optimized model)

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/AI-Virtual-Mouse.git
cd AI-Virtual-Mouse

# Install dependencies
pip install -r requirements.txt
```

## How It Works
1. Hand Detection: Uses OpenCV and MediaPipe to detect hand landmarks.
2. Gesture Recognition: A deep learning model interprets gestures.
3. Mouse Control: Pyautogui translates gestures into mouse actions.
4. UI Interface: Streamlit provides an interactive interface.
