def triage_patient(symptoms: str):
    symptoms = symptoms.lower()

    critical_keywords = [
        "unconscious", "not breathing", "collapse",
        "severe chest pain with sweating",
        "stroke", "paralysis", "seizure"
    ]

    urgent_keywords = [
        "chest pain", 
        "shortness of breath",
        "high fever",
        "persistent vomiting",
        "severe headache",
        "blurred vision"
    ]

    # CRITICAL LEVEL
    for word in critical_keywords:
        if word in symptoms:
            return {
                "level": "CRITICAL",
                "color": "red",
                "action": "Seek emergency medical help immediately"
            }

    # URGENT LEVEL
    for word in urgent_keywords:
        if word in symptoms:
            return {
                "level": "URGENT",
                "color": "orange",
                "action": "See a doctor within 24 hours"
            }

    # LOW RISK
    return {
        "level": "LOW RISK",
        "color": "green",
        "action": "Home care or routine clinic visit"
    }