import pandas as pd
import joblib
import os
import re

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_PATH = os.path.join(BASE_DIR, "training", "dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "models", "disease_model.pkl")

os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

# -------------------------
# CLEAN FUNCTION
# -------------------------
def clean(text):
    text = str(text).lower()
    text = re.sub(r"[^a-z ]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------
# LOAD DATA
# -------------------------
df = pd.read_csv(DATA_PATH)

df["symptoms"] = df["symptoms"].apply(clean)
df["disease"] = df["disease"].str.lower().str.strip()

X = df["symptoms"]
y = df["disease"]

# -------------------------
# TRAIN SPLIT (STRATIFIED)
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -------------------------
# MODEL (IMPROVED)
# -------------------------
model = Pipeline([
    ("tfidf", TfidfVectorizer(
        ngram_range=(1, 3),   # BIG UPGRADE (captures medical phrases)
        max_features=3000,
        stop_words="english"
    )),
    ("clf", LogisticRegression(
        max_iter=500,
        class_weight="balanced"
    ))
])

# -------------------------
# TRAIN
# -------------------------
model.fit(X_train, y_train)

# -------------------------
# SAVE
# -------------------------
joblib.dump(model, MODEL_PATH)

print("✅ Hospital AI v4 model trained successfully")