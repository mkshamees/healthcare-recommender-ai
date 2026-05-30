import joblib
import numpy as np

model = joblib.load("models/disease_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


MEDICINE_MAP = {
    "diabetes": ["Metformin", "Insulin"],
    "flu": ["Paracetamol", "Rest", "Fluids"],
    "malaria": ["Artemether/Lumefantrine"],
    "heart disease": ["Aspirin", "Beta blockers"],
    "hypertension": ["Amlodipine", "Lisinopril"]
}


def predict_disease(symptoms: str):
    X = vectorizer.transform([symptoms])

    prediction = model.predict(X)[0]
    prob = np.max(model.predict_proba(X)) if hasattr(model, "predict_proba") else None

    return prediction, float(prob) if prob else 0.0


def recommend_medicine(disease: str):
    return MEDICINE_MAP.get(disease, ["Consult a doctor"])