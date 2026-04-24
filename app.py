import streamlit as st
import pickle
import numpy as np

# تحميل الموديل - تأكدي إن الملف ده موجود جنبه على الديسكتوب
model = pickle.load(open('diabetes_model (7).pkl', 'rb'))

st.title("نظام التنبؤ بالسكري")

# خانات إدخال البيانات
glucose = st.number_input("نسبة الجلوكوز", value=100)
bmi = st.number_input("مؤشر كتلة الجسم BMI", value=25.0)
age = st.number_input("العمر", value=30)

if st.button("تحليل النتيجة"):
    # ترتيب البيانات لازم يكون زي ما الموديل اتدرب عليه
    features = np.array([[glucose, bmi, age]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة إيجابية")
    else:
        st.success("النتيجة سلبية")