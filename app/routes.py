from flask import Blueprint, render_template, request, jsonify

from app.services.predictor import predict_disease
from app.services.recommendations import recommend_medicine
from app.services.triage import triage_level
from app.services.emergency import is_emergency

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# ----------------------------
# MAIN PREDICT API
# ----------------------------
@main.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    symptoms = data.get("symptoms", "")
    user_id = data.get("user_id", 0)

    # 1. emergency check
    if is_emergency(symptoms):
        return jsonify({
            "status": "EMERGENCY",
            "message": "Seek immediate medical attention immediately",
            "action": "Go to nearest hospital"
        })

    # 2. disease prediction
    result = predict_disease(symptoms)
    disease = result.get("disease")

    # 3. triage
    severity = triage_level(symptoms)

    # 4. medicine recommendation
    meds = recommend_medicine(disease)

    return jsonify({
        "user_id": user_id,
        "symptoms": symptoms,
        "prediction": result,
        "severity": severity,
        "treatment": meds
    })