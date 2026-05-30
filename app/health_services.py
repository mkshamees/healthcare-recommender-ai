import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

medicine_path = os.path.join(BASE_DIR, "medicine_recommendation_dataset.csv")

medicine_map = {}

if os.path.exists(medicine_path):
    df = pd.read_csv(medicine_path)
    medicine_map = df.groupby("Disease")["Medicine"].apply(list).to_dict()


def recommend_medicine(disease):
    if not disease:
        return ["Invalid input"]
    return medicine_map.get(disease.lower(), ["Consult a doctor"])