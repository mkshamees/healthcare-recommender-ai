import os
import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# =============================
# BASE DIRECTORY
# =============================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================
# AUTO-FIND DATASET (NO STRUCTURE CHANGE)
# =============================
possible_paths = [
    os.path.join(BASE_DIR, "training.csv"),
    os.path.join(BASE_DIR, "dataset.csv"),
    os.path.join(BASE_DIR, "data", "training.csv"),
]

DATA_PATH = os.path.join(BASE_DIR, "training", "dataset.csv")

for path in possible_paths:
    if os.path.exists(path):
        DATA_PATH = path
        break

if DATA_PATH is None:
    raise FileNotFoundError(
        "❌ training.csv not found. Put it in project root or training folder."
    )

print(f"📂 Using dataset: {DATA_PATH}")

# =============================
# LOAD DATA
# =============================
df = pd.read_csv(DATA_PATH)
df = df.dropna()

X = df["symptoms"].astype(str)
y = df["disease"].astype(str)

# =============================
# TEXT VECTORISATION
# =============================
vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

# =============================
# SAFE STRATIFY LOGIC
# =============================
class_counts = y.value_counts()

if class_counts.min() < 2:
    stratify = None
else:
    stratify = y

# =============================
# TRAIN TEST SPLIT
# =============================
X_train, X_test, y_train, y_test = train_test_split(
    X_vec,
    y,
    test_size=0.3,
    random_state=42,
    stratify=stratify
)

# =============================
# MODEL
# =============================
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# =============================
# EVALUATION
# =============================
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model trained successfully")
print(f"📊 Accuracy: {accuracy * 100:.2f}%")

# =============================
# SAVE MODEL
# =============================
MODEL_DIR = os.path.join(BASE_DIR, "app", "models")
os.makedirs(MODEL_DIR, exist_ok=True)

joblib.dump(model, os.path.join(MODEL_DIR, "disease_model.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_DIR, "vectorizer.pkl"))

print("💾 Model saved to app/models/")