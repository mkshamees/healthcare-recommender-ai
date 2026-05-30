def is_emergency(symptoms):
    s = str(symptoms).lower()

    return any(x in s for x in [
        "chest pain",
        "not breathing",
        "unconscious",
        "stroke",
        "severe bleeding"
    ])