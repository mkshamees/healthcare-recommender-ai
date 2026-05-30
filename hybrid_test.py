def simple_cf(user_id, disease):
    return 4.2


def recommend_medicine(disease):
    return ["Consult doctor"]


def hybrid_system(user_id, disease):

    meds = recommend_medicine(disease)
    cf_score = simple_cf(user_id, disease)

    return {
        "user_id": user_id,
        "disease": disease,
        "medicines": meds,
        "score": cf_score
    }


print(hybrid_system(1, "Diabetes"))