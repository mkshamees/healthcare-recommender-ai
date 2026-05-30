import os
import joblib
import numpy as np
from app.services.disease_info import DISEASE_INFO

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.pkl")
VECT_PATH = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = None
vectorizer = None

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECT_PATH)
    print("✅ Hospital AI model loaded")
except:
    print("❌ Model not loaded - fallback mode active")


def clean_text(text):
    return text.lower().strip()


def predict_disease(symptoms: str):
    symptoms = clean_text(symptoms)

    # fallback if model missing
    if model is None or vectorizer is None:
        return {
            "disease": "flu",
            "confidence": 50,
            "status": "fallback"
        }

    X = vectorizer.transform([symptoms])

    # TOP 3 PREDICTIONS
    probs = model.predict_proba(X)[0]
    classes = model.classes_

    top_indices = np.argsort(probs)[::-1][:3]

    results = []
    for i in top_indices:
        results.append({
            "disease": classes[i],
            "confidence": round(float(probs[i]) * 100, 2)
        })

    disease = results[0]["disease"]

    # ✅ MUST BE INSIDE FUNCTION
    info = DISEASE_INFO.get(
        disease,
        {
            "description": "No information available",
            "risk": "Unknown",
            "advice": "Consult a healthcare professional"
        }
    )

    return {
        "top_predictions": results,
        "disease": disease,
        "confidence": results[0]["confidence"],
        "description": info["description"],
        "risk": info["risk"],
        "advice": info["advice"],
        "status": "success"
    }