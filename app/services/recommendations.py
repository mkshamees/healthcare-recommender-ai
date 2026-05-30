def recommend_medicine(disease):
    db = {
        "flu": ["Paracetamol", "Rest", "Fluids"],
        "malaria": ["Artemether-Lumefantrine"],
        "diabetes": ["Metformin"],
        "heart disease": ["Refer to cardiologist"],
        "kidney disease": ["Refer to nephrologist"]
    }

    return db.get(str(disease).lower(), ["See doctor"])