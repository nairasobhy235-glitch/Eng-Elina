import streamlit as st
import pickle
import numpy as np
import os

# 1. تصحيح المسار واسم الملف (استخدمنا الاسم اللي في الصورة بالظبط)
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model (7).pkl')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"المشكلة في اسم ملف الموديل! تأكدي إن الملف اسمه: diabetes_model (7).pkl")
    st.stop()

st.title("نظام التنبؤ بالسكري - Eng Elina")

# 2. إنشاء الـ 17 خانة المطلوبة
inputs = []
cols = st.columns(3)
for i in range(1, 18):
    with cols[(i-1)%3]:
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"feat_{i}")
        inputs.append(val)

if st.button("Predict (تنبؤ)"):
    # تنفيذ التنبؤ باستخدام الـ 17 معلومة
    final_features = np.array([inputs])
    prediction = model.predict(final_features)
    
    st.divider()
    if prediction[0] == 1:
        st.error("### النتيجة: الشخص مصاب بالسكري")
    else:
        st.success("### النتيجة: الشخص سليم")
