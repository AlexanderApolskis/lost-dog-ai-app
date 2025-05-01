# 🐾 Lost Dog Finder AI App

Welcome to the **Lost Dog Finder AI App**, created by **E. Alexander Apolskis** for the **AFM - Personal Project**. This is a powerful, AI-powered community platform to help reunite lost dogs with their owners through real-time uploads, intelligent classification, and beautiful UI. 📸🐶

---

## ✨ Features

- 📷 Upload photos of a dog and receive an AI-based prediction: **Lost** or **Found**
- 🏷️ Label dogs as Lost, Found, or Reunited
- 🆕 NEW badge for dogs posted within the last 24 hours
- 🔍 Search/filter by name, city, or status
- 🎉 Celebrate reunions via the "Mark as Reunited" feature
- 🌟 View Success Stories of dogs that made it home
- 📍 Find nearby shelters using smart filtering
- 📱 Built for mobile, deployable via ngrok for live demo or phone uploads

---

## 🧠 AI Model Details

- Built using **Keras** + **TensorFlow**
- Binary classifier model: outputs a probability (0 to 1)
- Image pre-processing:
  - Resized to 224x224
  - Normalized pixel values
  - Converted to batch tensor
- Prediction logic:
```python
prediction = model.predict(input_data)[0][0]
if prediction > 0.5:
    label = "Found dog"
else:
    label = "Lost dog"
