# 🧬 Fingerprint-based Blood Group Detection

> 🎯 This is a machine learning-based project that predicts a person’s blood group using their fingerprint image. It uses a custom-trained deep learning model with no external APIs — deployed locally via Flask, fully offline and privacy-friendly.

> 🚫 No APIs. No third-party services. Just my own trained machine learning model, built from scratch and deployed using only Flask and basic tools — fully offline.

## 🚀 Inspiration
During a hackathon where the use of external APIs and cloud services was restricted, we decided to build an AI-based healthcare solution entirely from scratch. Blood group identification is crucial in medical emergencies like transfusions and surgeries, but traditional methods are invasive and time-consuming. Inspired by the potential of biometrics and machine learning, we developed a fast, non-invasive, and intelligent system that predicts blood group from fingerprint images — using only our own trained model and local resources.

## 💡 What it does
This project uses a custom-trained machine learning model to predict a person's blood group from their fingerprint image. The user uploads a fingerprint scan, and the system returns the predicted blood group — all without any external API calls. It’s a novel, privacy-focused, and intelligent application of deep learning in biometric health prediction.

## 🛠️ How we built it
- **Dataset**: A fingerprint dataset labeled with corresponding blood groups.
- **Preprocessing**: Resized, normalized, and augmented the images to improve generalization.
- **Model**: A Convolutional Neural Network (CNN) trained using TensorFlow/Keras.
- **Deployment**: The trained `.keras` model was deployed with Flask and HTML to create a lightweight web interface for real-time predictions.

### 📁 Project Structure

```
├── app.py
├── model/
│ └── model.keras
├── uploads/
├── template/
│ └── index.html
├── static/
├── dataset/
├── notebook.ipynb
└── README.md
```

## ⚙️ Tech Stack
- **Python** – Core programming language
- **TensorFlow/Keras** – For building and training the CNN model
- **NumPy & PIL** – For image preprocessing
- **Flask** – Backend web framework for deployment
- **HTML & CSS** – For frontend interface
- **Jupyter Notebook** – For model experimentation and development
- **Git & GitHub** – For version control and project hosting

## 🚧 Challenges we ran into
- Finding a clean and labeled fingerprint dataset with accurate blood group annotations.
- Training a robust model that generalizes well to new fingerprint samples.
- Handling noise, inconsistencies, and variations in fingerprint images.
- Ensuring smooth file uploads and local model inference in Flask.

## 🏆 Accomplishments that we're proud of
- Built a deep learning model that accurately predicts blood group from biometric input.
- Deployed a complete ML system without using any third-party APIs.
- Designed a user-friendly web interface using only basic tools.
- Completed the entire project under hackathon constraints using our own resources.

## 📚 What we learned
- How to design and train CNNs for image classification using TensorFlow/Keras.
- Local deployment of ML models using Flask and Python.
- Managing end-to-end ML pipelines — from data preprocessing to web deployment.
- File handling, routing, and UI integration in Flask-based web applications.
