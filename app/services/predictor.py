import os
import joblib

from app.core.medical_mapper import normalize_symptoms

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
    print("✅ Hospital AI model loaded")
except Exception as e:
    model = None
    print("❌ Model load failed:", e)


def predict_disease(symptoms):

    symptoms = normalize_symptoms(symptoms)

    if not symptoms.strip():
        return {
            "disease": "unknown",
            "confidence": 0,
            "status": "empty_input"
        }

    if model is None:
        return {
            "disease": "flu",
            "confidence": 50,
            "status": "fallback"
        }

    try:
        pred = model.predict([symptoms])[0]

        confidence = 0
        if hasattr(model, "predict_proba"):
            confidence = float(max(model.predict_proba([symptoms])[0]) * 100)

        return {
            "disease": pred,
            "confidence": round(confidence, 2),
            "status": "success"
        }

    except Exception as e:
        return {
            "disease": "unknown",
            "confidence": 0,
            "status": str(e)
        }