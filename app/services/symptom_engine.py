# app/services/symptom_engine.py

SEVERITY_WEIGHTS = {
    "chest pain": 5,
    "shortness of breath": 5,
    "unconscious": 5,
    "seizure": 5,

    "high fever": 3,
    "severe headache": 3,
    "vomiting": 3,

    "fever": 2,
    "cough": 1,
    "fatigue": 1,
    "dizziness": 2,
    "pain": 2
}


def calculate_risk_score(symptoms: str):
    """
    Returns a clinical risk score (0–10+)
    """
    if not symptoms:
        return 0

    s = symptoms.lower()
    score = 0

    for symptom, weight in SEVERITY_WEIGHTS.items():
        if symptom in s:
            score += weight

    return score


def interpret_risk(score: int):
    """
    Converts score to clinical category
    """
    if score >= 8:
        return "EMERGENCY"
    elif score >= 5:
        return "HIGH"
    elif score >= 2:
        return "MEDIUM"
    else:
        return "LOW"