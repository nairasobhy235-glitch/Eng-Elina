import streamlit as st
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model (7).pkl')

st.title("نظام التنبؤ بمرض السكري 🩺")

# إنشاء 8 خانات عشان الموديل يشتغل صح
pregnancies = st.number_input("Pregnancies", value=0)
glucose = st.number_input("Glucose", value=120)
blood_pressure = st.number_input("Blood Pressure", value=70)
skin_thickness = st.number_input("Skin Thickness", value=20)
insulin = st.number_input("Insulin", value=80)
bmi = st.number_input("BMI", value=28.0)
dpf = st.number_input("Diabetes Pedigree Function", value=0.5)
age = st.number_input("Age", value=30)

if st.button("Predict"):
    # تجميع الـ 8 مدخلات في قائمة واحدة
    features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    
    # التوقع
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: إيجابي (لديك احتمالية إصابة)")
    else:
        st.success("النتيجة: سلبي (أنت بصحة جيدة)")
