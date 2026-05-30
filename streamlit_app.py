import streamlit as st

from app.services.predictor import predict_disease
from app.services.recommendations import recommend_medicine
from app.services.emergency import is_emergency

st.set_page_config(
    page_title="🏥 Hospital AI",
    layout="centered"
)

st.title("🏥 Hospital AI System")
st.write("AI-powered disease prediction system")

symptoms = st.text_area("Enter symptoms (e.g fever, cough, headache)")

if st.button("Analyze"):

    if not symptoms.strip():
        st.warning("Please enter symptoms")
        st.stop()

    if is_emergency(symptoms):
        st.error("🚨 EMERGENCY DETECTED - SEEK MEDICAL HELP")
        st.stop()

    result = predict_disease(symptoms)

    st.subheader("🧠 Primary Diagnosis")
    st.success(result["disease"])

    st.subheader("📊 Confidence")
    st.write(f"{result['confidence']}%")

    st.subheader("🏥 Top 3 Predictions")
    for item in result.get("top_predictions", []):
        st.write(f"• {item['disease']} — {item['confidence']}%")

    st.subheader("💊 Treatment Suggestion")
    st.write(recommend_medicine(result["disease"]))

    st.subheader("📖 Disease Information")
    st.write(result.get("description"))

    st.subheader("⚠️ Risk Level")
    st.warning(result.get("risk"))

    st.subheader("📋 Medical Advice")
    st.info(result.get("advice"))

    report_text = f"""
PATIENT HEALTH REPORT

Symptoms:
{symptoms}

Predicted Disease:
{result['disease']}

Confidence:
{result['confidence']}%

Risk:
{result['risk']}

Advice:
{result['advice']}
"""

    st.download_button(
        label="📄 Download Report",
        data=report_text,
        file_name="health_report.txt",
        mime="text/plain"
    )

    st.json(result)