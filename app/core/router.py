def route_symptoms(symptoms: str):

    s = symptoms.lower()

    # HEART CONDITIONS
    if any(x in s for x in ["chest pain", "heart", "breathlessness", "arm pain"]):
        return "heart"

    # DIABETES
    if any(x in s for x in ["sugar", "thirst", "urination", "glucose"]):
        return "diabetes"

    # KIDNEY
    if any(x in s for x in ["back pain", "urine", "swelling", "kidney"]):
        return "kidney"

    # DEFAULT
    return "general"