import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Check if model file exists
MODEL_PATH = "model/model.keras"
if not os.path.exists(MODEL_PATH):
    st.error(f"❌ Model file not found at '{MODEL_PATH}'")
    st.stop()

# Load the model
with st.spinner("🔄 Loading model..."):
    model = tf.keras.models.load_model(MODEL_PATH)

# Blood group labels
class_names = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']

# Image preprocessing function
def preprocess_image(image):
    image = image.convert('RGB')
    image = image.resize((64, 64))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# UI config and style
st.set_page_config(page_title="BioPrint", page_icon="🩸")
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stButton>button { border-radius: 8px; background-color: #e63946; color: white; font-weight: bold; }
    .stTextInput>div>input, .stNumberInput>div>input {
        border: 1px solid #ccc; border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🩸 BioPrint")
st.subheader("No needles. Just touch — blood group detection through fingerprints.")

# Input form
with st.form("blood_form"):
    name = st.text_input("Name")
    mobile = st.text_input("Mobile")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    fingerprint_file = st.file_uploader("Upload Fingerprint", type=["jpg", "jpeg", "png", "bmp"])
    submitted = st.form_submit_button("Detect Blood Group")

# Prediction
if submitted:
    if fingerprint_file is not None:
        image = Image.open(fingerprint_file)
        st.image(image, caption="Uploaded Fingerprint", width=150)

        # Preprocess and predict
        img_array = preprocess_image(image)
        prediction = model.predict(img_array)[0]
        predicted_class = class_names[np.argmax(prediction)]
        confidence = float(np.max(prediction))

        # Show results
        st.success("✅ Detection Complete")
        st.write("### Prediction Summary")
        st.table({
            "Field": ["Name", "Mobile", "Gender", "Age", "Confidence", "Blood Group"],
            "Value": [name, mobile, gender, age, f"{confidence:.2f}", predicted_class]
        })
    else:
        st.warning("⚠️ Please upload a fingerprint image to continue.")
