import cv2
import numpy as np
import tensorflow as tf

IMG_SIZE = 224
MODEL_PATH = 'dog_match_model.h5'
IMAGE_PATH = 'test_image.jpg'  # Change this to your image

# Load the trained model
model = tf.keras.models.load_model(MODEL_PATH)

# Load and preprocess test image
img = cv2.imread(IMAGE_PATH)
resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
normalized = resized / 255.0
input_data = np.expand_dims(normalized, axis=0)

# Predict
prediction = model.predict(input_data)[0][0]
confidence = round(prediction * 100, 2)

if prediction > 0.5:
    print(f"🐾 Prediction: FOUND dog ({confidence}% confidence)")
else:
    print(f"🐾 Prediction: LOST dog ({100 - confidence}% confidence)")
