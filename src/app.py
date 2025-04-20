import streamlit as st
try:
    import cv2
    st.success("✅ OpenCV loaded successfully!")
except ModuleNotFoundError:
    st.error("❌ OpenCV module not found.")
import mediapipe as mp
from gcpy import GestureController, HandRecog, HLabel, Gest, Controller  # Assuming your class is in gcpy.py

st.set_page_config(page_title="Gesture Controller App", layout="centered")

st.title("🤖 Gesture Controller Live Stream")

# Add a placeholder for the camera feed
frame_placeholder = st.empty()

# Start Gesture Controller
gc = GestureController()

# Display instructions or info
st.markdown("Click the 'Stop Stream' button to quit the live stream.")

# Button to stop the stream
stop_button = st.button("Stop Stream")

# Overriding the GestureController's `start()` to show in Streamlit
def start_streamlit_mode():
    handmajor = HandRecog(HLabel.MAJOR)
    handminor = HandRecog(HLabel.MINOR)

    mp_hands_module = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils

    with mp_hands_module.Hands(max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while gc.gc_mode:
            if stop_button:
                st.write("Stopping the stream...")
                break  # Exit the loop when the button is clicked

            success, image = gc.cap.read()
            if not success:
                continue

            image = cv2.flip(image, 1)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_image)

            if results.multi_hand_landmarks:
                gc.classify_hands(results)

                handmajor.update_hand_result(gc.hr_major)
                handminor.update_hand_result(gc.hr_minor)

                handmajor.set_finger_state()
                handminor.set_finger_state()

                gest_name = handminor.get_gesture()
                if gest_name == Gest.PINCH_MINOR:
                    Controller.handle_controls(gest_name, handminor.hand_result)
                else:
                    gest_name = handmajor.get_gesture()
                    Controller.handle_controls(gest_name, handmajor.hand_result)

                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands_module.HAND_CONNECTIONS)
            else:
                Controller.prev_hand = None

            # Show the image in Streamlit
            frame_placeholder.image(image, channels="BGR", use_container_width=True)

            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

    gc.cap.release()
    cv2.destroyAllWindows()

start_streamlit_mode()
