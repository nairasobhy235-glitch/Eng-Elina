import streamlit as st
import joblib
import numpy as np

# تحميل الموديل باستخدام joblib (الأضمن)
try:
    model = joblib.load('diabetes_model (7).pkl')
except Exception as e:
    st.error(f"Error loading model: {e}")

st.title("نظام التنبؤ بمرض السكري - Eng Elina")

# المدخلات المطلوبة (8 مدخلات حسب صورك)
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", value=0)
    glucose = st.number_input("Glucose", value=100)
    bp = st.number_input("Blood Pressure", value=70)
    skin = st.number_input("Skin Thickness", value=20)

with col2:
    insulin = st.number_input("Insulin", value=79)
    bmi = st.number_input("BMI", value=25.0)
    dpf = st.number_input("Pedigree Function", value=0.47)
    age = st.number_input("Age", value=30)

if st.button("Predict (تنبؤ)"):
    # تجميع المدخلات في مصفوفة
    features = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: إيجابي (Positive) - يوجد احتمالية إصابة")
    else:
        st.success("النتيجة: سلبي (Negative) - الحالة مستقرة")
