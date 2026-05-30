def clean_symptoms(text: str):
    if not text:
        return ""

    text = text.lower().strip()

    replacements = {
        "feverish": "fever",
        "breathless": "difficulty breathing",
        "sugar problem": "diabetes",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text