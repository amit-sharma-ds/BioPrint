# 🧬 Fingerprint-based Blood Group Detection

> 🎯 This is a machine learning-based project that predicts a person’s blood group using their fingerprint image. It uses a custom-trained deep learning model with no external APIs — deployed using Streamlit, fully offline and privacy-friendly.

> 🚫 No APIs. No third-party services. Just my own trained machine learning model, built from scratch and deployed using only Streamlit and Python tools — fully offline.

## 🚀 Inspiration
During a hackathon where the use of external APIs and cloud services was restricted, we decided to build an AI-based healthcare solution entirely from scratch. Blood group identification is crucial in medical emergencies like transfusions and surgeries, but traditional methods are invasive and time-consuming. Inspired by the potential of biometrics and machine learning, we developed a fast, non-invasive, and intelligent system that predicts blood group from fingerprint images — using only our own trained model and local resources.

## 💡 What it does
This project uses a custom-trained machine learning model to predict a person's blood group from their fingerprint image. The user uploads a fingerprint scan, and the system returns the predicted blood group — all without any external API calls. It’s a novel, privacy-focused, and intelligent application of deep learning in biometric health prediction.

## 🛠️ How we built it
- **Dataset**: A fingerprint dataset labeled with corresponding blood groups.
- **Preprocessing**: Images were resized, normalized, and augmented using libraries like NumPy and PIL.
- **Model**: A Convolutional Neural Network (CNN) was designed and trained using TensorFlow and Keras. The final model achieved **90% training accuracy**, demonstrating strong learning capability on the dataset.
- **Visualization & EDA**: Used Pandas, Matplotlib, and Seaborn for exploratory data analysis and plotting insights.
- **Deployment**: The trained `.h5` or `.keras` model was deployed using **Streamlit**, creating a lightweight and interactive web app interface.

## 📁 Project Structure

```
├── app.py
├── model/
│ └── model.h5 / model.keras
├── uploads/
├── dataset/
├── static/ (optional for CSS/images)
├── notebook.ipynb
└── README.md
```


## ⚙️ Tech Stack
- **Python** – Core programming language
- **Streamlit** – For web app interface and deployment
- **TensorFlow/Keras** – For building and training the CNN model
- **NumPy & PIL** – For image preprocessing
- **Pandas** – For data handling and tabular operations
- **Matplotlib & Seaborn** – For visualizations and data insights
- **Jupyter Notebook** – For model experimentation and development
- **Git & GitHub** – For version control and project hosting

## 🧰 Built With
Python, Machine Learning, Streamlit, TensorFlow, Keras, NumPy, Pandas, Matplotlib, Seaborn, Jupyter Notebook, Git, GitHub

## 🚧 Challenges we ran into
- Finding a clean and labeled fingerprint dataset with accurate blood group annotations.
- Training a robust model that generalizes well to new fingerprint samples.
- Handling noise, inconsistencies, and variations in fingerprint images.
- Ensuring smooth file uploads and local model inference in Streamlit.

## 🏆 Accomplishments that we're proud of
- Built a deep learning model that accurately predicts blood group from biometric input.
- Achieved **90% training accuracy** on fingerprint image classification.
- Deployed a complete ML system without using any third-party APIs.
- Designed a user-friendly web interface using only local and open-source tools.
- Completed the entire project under hackathon constraints using our own resources.

## 📚 What we learned
- How to design and train CNNs for image classification using TensorFlow/Keras.
- Local deployment of ML models using Streamlit and Python.
- Managing end-to-end ML pipelines — from data preprocessing to deployment.
- File handling, user input, and UI design in Streamlit-based web applications.
