import streamlit as st
import joblib
import numpy as np

# تحميل الموديل بطريقة joblib الأضمن
try:
    model = joblib.load('diabetes_model (7).pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("نظام التنبؤ بمرض السكري 🩺")

# المدخلات (تأكدي من ترتيبها حسب الموديل)
glucose = st.number_input("Glucose", value=100)
bmi = st.number_input("BMI", value=25.0)
age = st.number_input("Age", value=30)

if st.button("Predict"):
    features = np.array([[glucose, bmi, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: إيجابي (Positive)")
    else:
        st.success("النتيجة: سلبي (Negative)")
