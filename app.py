from flask import Flask, request, render_template, redirect, url_for
import cv2
import numpy as np
import tensorflow as tf
import os
import json
import random

app = Flask(__name__)
MODEL_PATH = 'dog_match_model.h5'
IMG_SIZE = 224

# Load the model once on startup
model = tf.keras.models.load_model(MODEL_PATH)

# Load posts (helper function)
def load_posts():
    if os.path.exists('dog_posts.json'):
        with open('dog_posts.json', 'r') as file:
            return json.load(file)
    return []

@app.route('/')
def home():
    posts = load_posts()
    lost_dogs = [dog for dog in posts if dog.get('dog_status') == 'Lost']
    featured_dog = random.choice(lost_dogs) if lost_dogs else None
    return render_template('index.html', featured_dog=featured_dog)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return 'No image uploaded', 400

    file = request.files['image']
    if file.filename == '':
        return 'No selected file', 400

    filepath = os.path.join('static', 'uploaded.jpg')
    file.save(filepath)

    img = cv2.imread(filepath)
    resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    normalized = resized / 255.0
    input_data = np.expand_dims(normalized, axis=0)

    prediction = model.predict(input_data)[0][0]
    confidence = round(prediction * 100, 2)

    if prediction > 0.5:
        label = f"FOUND dog ({confidence}% confidence)"
    else:
        label = f"LOST dog ({100 - confidence}% confidence)"

    return render_template('result.html', label=label, image='uploaded.jpg')

# Register routes from routes.py
from routes.routes import routes
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
