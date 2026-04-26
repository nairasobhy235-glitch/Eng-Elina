
 import streamlit as st
import pickle
import numpy as np

# 1. تحميل الموديل
model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title("نظام التنبؤ بمرض السكري - Eng Elina")

# 2. إنشاء 17 خانة إدخال (موزعة على أعمدة ليكون شكلها منظماً)
col1, col2, col3 = st.columns(3)

with col1:
    f1 = st.number_input("Pregnancies", value=0)
    f4 = st.number_input("Skin Thickness", value=20)
    f7 = st.number_input("Pedigree Function", value=0.47)
    f10 = st.number_input("Feature 10", value=0.0)
    f13 = st.number_input("Feature 13", value=0.0)
    f16 = st.number_input("Feature 16", value=0.0)

with col2:
    f2 = st.number_input("Glucose", value=100)
    f5 = st.number_input("Insulin", value=79)
    f8 = st.number_input("Age", value=30)
    f11 = st.number_input("Feature 11", value=0.0)
    f14 = st.number_input("Feature 14", value=0.0)
    f17 = st.number_input("Feature 17", value=0.0)

with col3:
    f3 = st.number_input("Blood Pressure", value=70)
    f6 = st.number_input("BMI", value=25.0)
    f9 = st.number_input("Feature 9", value=0.0)
    f12 = st.number_input("Feature 12", value=0.0)
    f15 = st.number_input("Feature 15", value=0.0)

# 3. زر التنبؤ
if st.button("Predict (تنبؤ)"):
    # تجميع الـ 17 ميزة في قائمة واحدة بالترتيب الصحيح
    features = np.array([[f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13, f14, f15, f16, f17]])
    
    # إجراء التنبؤ
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: الشخص مصاب بالسكري")
    else:
        st.success("النتيجة: الشخص غير مصاب بالسكري")
