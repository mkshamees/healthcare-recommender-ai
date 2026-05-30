import streamlit as st

from app.services.predictor import predict_disease
from app.services.recommendations import recommend_medicine
from app.services.emergency import is_emergency

st.set_page_config(
    page_title="Hospital AI",
    page_icon="🏥",
    layout="centered"
)

st.title("🏥 Hospital AI")
st.write("Enter symptoms to receive an AI-assisted assessment.")

symptoms = st.text_area(
    "Symptoms",
    placeholder="Example: fever, cough, headache"
)

if st.button("Analyze"):

    if not symptoms.strip():
        st.warning("Please enter symptoms.")
        st.stop()

    try:

        if is_emergency(symptoms):
            st.error("🚨 Emergency symptoms detected. Seek immediate medical attention.")
            st.stop()

        result = predict_disease(symptoms)

        st.subheader("🧠 Predicted Condition")
        st.success(result.get("disease", "Unknown"))

        st.subheader("📈 Confidence")
        st.write(f"{result.get('confidence', 0)}%")

        if "category" in result:
            st.subheader("📊 Category")
            st.info(result["category"])

        if "risk" in result:
            st.subheader("⚠️ Risk Level")
            st.warning(result["risk"])

        st.subheader("💊 Recommendations")
        st.write(
            recommend_medicine(
                result.get("disease", "unknown")
            )
        )

        st.subheader("📄 Raw Result")
        st.json(result)

    except Exception as e:
        st.error(f"System Error: {str(e)}")