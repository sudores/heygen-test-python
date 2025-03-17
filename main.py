import cv2
import requests
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ensure model directory exists
MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "haarcascade_frontalface_default.xml")
MODEL_URL = "https://github.com/opencv/opencv/raw/4.x/data/haarcascades/haarcascade_frontalface_default.xml"

if not os.path.exists(MODEL_DIR):
    os.makedirs(MODEL_DIR)

# Download the model if not available
if not os.path.exists(MODEL_PATH):
    print("Downloading pre-trained model...")
    response = requests.get(MODEL_URL)
    with open(MODEL_PATH, "wb") as f:
        f.write(response.content)

print("Model ready!")

# Load model
face_cascade = cv2.CascadeClassifier(MODEL_PATH)

@app.route("/detect_faces", methods=["POST"])
def detect_faces():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image_file = request.files["image"]
    image_path = "uploaded_image.jpg"
    image_file.save(image_path)

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    return jsonify({"faces_detected": len(faces)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

