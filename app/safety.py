EMERGENCY_KEYWORDS = [
    "chest pain",
    "unconscious",
    "severe bleeding",
    "difficulty breathing",
    "stroke",
    "seizure"
]


def is_emergency(symptoms: str) -> bool:
    symptoms = symptoms.lower()
    return any(word in symptoms for word in EMERGENCY_KEYWORDS)