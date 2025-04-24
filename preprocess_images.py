import os
import cv2
import numpy as np

IMG_SIZE = 224
DATA_DIR = 'dataset'
CATEGORIES = ['lost', 'found']
SAVE_PATH = 'preprocessed_data.npy'

def preprocess_dataset():
    images = []
    labels = []

    for category in CATEGORIES:
        path = os.path.join(DATA_DIR, category)
        class_num = CATEGORIES.index(category)

        for img_name in os.listdir(path):
            if img_name == ".DS_Store":
                continue

            img_path = os.path.join(path, img_name)

            try:
                img_array = cv2.imread(img_path)
                if img_array is None:
                    raise ValueError("Image not readable")
                resized = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                normalized = resized / 255.0
                images.append(normalized)
                labels.append(class_num)
            except Exception as e:
                print(f"⚠️ Failed to process {img_name}: {e}")

    try:
        data = {"images": np.array(images), "labels": np.array(labels)}
        np.save(SAVE_PATH, data)
        print(f"✅ Saved {len(images)} images to {SAVE_PATH}")
    except Exception as e:
        print(f"❌ Error saving file: {e}")

if __name__ == "__main__":
    preprocess_dataset()
