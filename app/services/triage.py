def triage_level(symptoms):
    s = str(symptoms).lower()

    if any(x in s for x in ["chest pain", "stroke", "breathing"]):
        return "HIGH"

    if any(x in s for x in ["fever", "cough", "pain"]):
        return "MEDIUM"

    return "LOW"