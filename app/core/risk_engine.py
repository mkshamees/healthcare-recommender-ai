def calculate_risk(symptoms: str):

    s = symptoms.lower()

    risk = 0

    critical = ["chest pain", "unconscious", "severe bleeding", "stroke"]
    high = ["breathing", "vomiting", "swelling"]
    medium = ["fever", "pain", "cough", "fatigue"]

    risk += 60 * any(x in s for x in critical)
    risk += 30 * any(x in s for x in high)
    risk += 10 * any(x in s for x in medium)

    if risk >= 60:
        return "CRITICAL"
    elif risk >= 30:
        return "HIGH"
    elif risk >= 10:
        return "MEDIUM"
    return "LOW"