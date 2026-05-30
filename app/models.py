def clinical_decision(symptoms, ml_result):
    """
    Combines ML + clinical risk scoring
    """

    from app.services.symptom_engine import calculate_risk_score, interpret_risk

    risk_score = calculate_risk_score(symptoms)
    risk_level = interpret_risk(risk_score)

    disease = ml_result.get("disease", "unknown")
    confidence = ml_result.get("confidence", 0)

    # 🚨 OVERRIDE RULE 1: Emergency always wins
    if risk_level == "EMERGENCY":
        return {
            "final_diagnosis": disease,
            "risk_level": risk_level,
            "action": "EMERGENCY - GO TO HOSPITAL",
            "confidence": confidence
        }

    # ⚠️ OVERRIDE RULE 2: Low confidence → doctor
    if confidence < 60:
        return {
            "final_diagnosis": disease,
            "risk_level": risk_level,
            "action": "SEE DOCTOR",
            "confidence": confidence
        }

    return {
        "final_diagnosis": disease,
        "risk_level": risk_level,
        "action": "STANDARD CARE",
        "confidence": confidence
    }