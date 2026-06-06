import streamlit as st
from utils import predict

st.set_page_config(page_title="Medical AI", layout="centered")

st.title("🧠 Intelligent Medical Report Analyzer")

text = st.text_area("📄 Enter Medical Report")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter report")
    else:
        label, confidence = predict(text)

        st.success(f"🩺 Specialty: {label}")
        st.info(f"📊 Confidence: {confidence:.2f}")

        st.subheader("🔍 Important Keywords")
        words = text.split()[:10]
        st.write(words)
