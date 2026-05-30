def is_emergency(symptoms: str):
    symptoms = symptoms.lower()

    emergency_keywords = [
        "severe chest pain",
        "unconscious",
        "cannot breathe",
        "stopping breathing",
        "stroke",
        "paralysis",
        "heavy chest pain with sweating",
        "collapse",
        "severe shortness of breath at rest"
    ]

    # only trigger emergency if strong combination exists
    for keyword in emergency_keywords:
        if keyword in symptoms:
            return True

    return False