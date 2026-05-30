def normalize_symptoms(text: str):

    text = str(text).lower()

    mapping = {
        "shortness breath": "difficulty breathing",
        "breath short": "difficulty breathing",
        "chest pain": "chest pain",
        "blurred vision": "vision problem",
        "frequent urination": "urination frequent",
        "excessive thirst": "thirst excessive",
        "swollen legs": "leg swelling",
        "fatigue": "tiredness",
        "high fever": "fever high"
    }

    for k, v in mapping.items():
        text = text.replace(k, v)

    return text