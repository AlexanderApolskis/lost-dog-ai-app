# 🐶 Lost Dog Finder AI App

## 📋 Project Description
This Flask web app helps reunite lost dogs with their owners using AI image classification and community posts. Users can upload photos of lost/found dogs, receive AI predictions, and browse local shelter listings. Mobile-ready and ngrok-enabled for live demos.

Built with **Flask**, **TensorFlow**, **OpenCV**, and **HTML/CSS**.

---

## 🚀 Features
- Upload dog photos for AI-based Lost/Found classification
- Post missing or found dogs with contact info and photo
- View current dog listings (Lost, Found, Reunited)
- Mark dogs as “Reunited” with a success story flow
- Display shelter-submitted dogs with hours & logos
- Mobile-optimized for fast camera uploads and sharing
- Public access via ngrok for live mobile demos

---

## 🛠️ How to Run
1. Clone this repository to your computer:

    ```bash
    git clone https://github.com/YOUR_USERNAME/lost-dog-ai-app.git
    ```

2. Move into the project folder:

    ```bash
    cd lost-dog-ai-app
    ```

3. Set up a virtual environment and install required packages:

    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    pip install -r requirements.txt
    ```

4. Launch the app locally:

    ```bash
    python app.py
    ```

5. (Optional) Make it public on mobile using:

    ```bash
    ngrok http 5000
    ```

---

## 📂 Project Structure

