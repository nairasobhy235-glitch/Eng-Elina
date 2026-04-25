import streamlit as st
import joblib
import numpy as np

# تحميل الموديل
model = joblib.load('diabetes_model (7).pkl')

st.title("Eng Elina - نظام التنبؤ بالسكري")

# إنشاء 8 خانات للإدخال
col1, col2 = st.columns(2)
with col1:
    preg = st.number_input("Pregnancies", value=0)
    glu = st.number_input("Glucose", value=100)
    bp = st.number_input("Blood Pressure", value=70)
    skin = st.number_input("Skin Thickness", value=20)
with col2:
    ins = st.number_input("Insulin", value=79)
    bmi = st.number_input("BMI", value=25.0)
    dpf = st.number_input("Pedigree Function", value=0.47)
    age = st.number_input("Age", value=30)

if st.button("Predict (تنبؤ)"):
    # تجميع الـ 8 مدخلات في قائمة واحدة
    features = np.array([[preg, glu, bp, skin, ins, bmi, dpf, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: Positive (يوجد احتمالية إصابة)")
    else:
        st.success("النتيجة: Negative (الحالة سليمة)")
