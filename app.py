import streamlit as st
import pickle
import numpy as np
import os

# 1. إعداد المسار الصحيح (تأكدي من وجود شرطتين من كل جانب لـ _file_)
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model.sav')

# تحميل الموديل
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("ملف الموديل diabetes_model.sav غير موجود بجانب الكود!")
    st.stop()

st.title("نظام التنبؤ بمرض السكري - Eng Elina")

# 2. إنشاء الـ 17 خانة
inputs = []
col1, col2, col3 = st.columns(3)

with col1:
    for i in range(1, 7):
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"v{i}")
        inputs.append(val)
with col2:
    for i in range(7, 13):
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"v{i}")
        inputs.append(val)
with col3:
    for i in range(13, 18):
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"v{i}")
        inputs.append(val)

# 3. زر التنبؤ
if st.button("Predict"):
    features = np.array([inputs])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: مصاب")
    else:
        st.success("النتيجة: سليم")
