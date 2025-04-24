# Lost Dog AI App 🐶

This web app helps match lost dogs to their owners using image recognition and machine learning.

## Features
- Upload dog images to compare with a trained model
- Real-time image matching using a neural network
- Flask-based web server with HTML templates

## Project Structure
- `app.py` – main Flask app
- `routes/` – routing logic
- `templates/` – HTML pages
- `static/` – CSS/images
- `predict.py`, `train_model.py` – ML logic
- `dog_match_model.h5` – model (not included in repo due to size)

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
