import streamlit as st
import joblib
import numpy as np

# تحميل الموديل
try:
    model = joblib.load('diabetes_model (7).pkl')
except:
    st.error("تأكد من رفع ملف الموديل بشكل صحيح")

st.title("نظام التنبؤ بمرض السكري 🩺")

# المدخلات الأساسية
pregnancies = st.number_input("Pregnancies", value=0)
glucose = st.number_input("Glucose", value=100)
blood_pressure = st.number_input("Blood Pressure", value=70)
skin_thickness = st.number_input("Skin Thickness", value=20)
insulin = st.number_input("Insulin", value=79)
bmi = st.number_input("BMI", value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", value=0.47)
age = st.number_input("Age", value=30)

if st.button("Predict"):
    # تجميع كل الـ 8 مدخلات اللي الموديل مستنيها
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: احتمال وجود سكري (Positive)")
    else:
        st.success("النتيجة: لا يوجد سكري (Negative)")
