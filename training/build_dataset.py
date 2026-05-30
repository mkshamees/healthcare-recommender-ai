import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

OUTPUT_PATH = os.path.join(BASE_DIR, "training", "dataset.csv")

# ---------------------------------------------------
# 1. SYNTHETIC GENERAL DISEASE DATA (baseline)
# ---------------------------------------------------
general_data = [
    ("fever cough headache body pain", "flu"),
    ("high fever chills sweating", "malaria"),
    ("frequent urination excessive thirst", "diabetes"),
    ("chest pain shortness of breath", "heart_disease"),
    ("swollen legs fatigue reduced urine", "kidney_disease"),
    ("headache blurred vision dizziness", "hypertension"),
    ("nausea vomiting abdominal pain", "food_poisoning"),
]

# ---------------------------------------------------
# 2. EXPAND DATASET (data augmentation)
# ---------------------------------------------------
expanded = []

for symptoms, disease in general_data:
    words = symptoms.split()

    # create variations
    for i in range(len(words)):
        variation = " ".join(words[:i] + words[i+1:])
        expanded.append((variation, disease))

    expanded.append((symptoms, disease))

# ---------------------------------------------------
# 3. LOAD YOUR EXISTING DATASETS (if available)
# ---------------------------------------------------
def load_external(file_path, disease_label):
    if not os.path.exists(file_path):
        return []

    df = pd.read_csv(file_path)

    if "symptoms" not in df.columns:
        return []

    return [(str(s).lower(), disease_label) for s in df["symptoms"].dropna()]


heart_path = os.path.join(BASE_DIR, "models", "heart.csv")
kidney_path = os.path.join(BASE_DIR, "models", "kidney.csv")
diabetes_path = os.path.join(BASE_DIR, "models", "diabetes.csv")

external = []
external += load_external(heart_path, "heart_disease")
external += load_external(kidney_path, "kidney_disease")
external += load_external(diabetes_path, "diabetes")


# ---------------------------------------------------
# 4. MERGE ALL DATA
# ---------------------------------------------------
final_data = expanded + external

df = pd.DataFrame(final_data, columns=["symptoms", "disease"])

# clean
df = df.dropna()
df["symptoms"] = df["symptoms"].str.lower()

# shuffle
df = df.sample(frac=1).reset_index(drop=True)

# ---------------------------------------------------
# 5. SAVE DATASET
# ---------------------------------------------------
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

df.to_csv(OUTPUT_PATH, index=False)

print("✅ Unified dataset created!")
print("Total samples:", len(df))
print("Saved to:", OUTPUT_PATH)
print("\nClass distribution:\n", df["disease"].value_counts())