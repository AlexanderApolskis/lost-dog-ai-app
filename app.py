from flask import Flask, request, render_template
import cv2
import numpy as np
import tensorflow as tf
import os

app = Flask(__name__)
MODEL_PATH = 'dog_match_model.h5'
IMG_SIZE = 224

# Load the model once on startup
model = tf.keras.models.load_model(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    # Save the uploaded image temporarily
    filepath = os.path.join('static', 'uploaded.jpg')
    file.save(filepath)

    # Preprocess image
    img = cv2.imread(filepath)
    resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    normalized = resized / 255.0
    input_data = np.expand_dims(normalized, axis=0)

    # Predict
    prediction = model.predict(input_data)[0][0]
    confidence = round(prediction * 100, 2)

    if prediction > 0.5:
        label = f"FOUND dog ({confidence}% confidence)"
    else:
        label = f"LOST dog ({100 - confidence}% confidence)"

    return render_template('result.html', label=label, image='uploaded.jpg')

if __name__ == '__main__':
    app.run(debug=True)
