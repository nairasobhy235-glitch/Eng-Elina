import streamlit as st
import pickle
import numpy as np
import os

# 1. إعداد مسار الموديل (تأكدي من وجود شرطتين تحت قبل وبعد كلمة file)
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model.sav')

# تحميل الموديل
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("ملف diabetes_model.sav مش موجود! ارفعيه على جيت هاب في نفس الفولدر")
    st.stop()

st.title("نظام التنبؤ بمرض السكري - Eng Elina")

# 2. إنشاء الـ 17 خانة (عشان الموديل ميزعلش)
inputs = []
cols = st.columns(3) # تقسيم الخانات على 3 أعمدة عشان الشكل يبق نضيف

for i in range(1, 18):
    with cols[(i-1)%3]:
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"v{i}")
        inputs.append(val)

# 3. زر التنبؤ
if st.button("Predict (تنبؤ)"):
    features = np.array([inputs])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("النتيجة: الشخص مصاب بالسكري")
    else:
        st.success("النتيجة: الشخص سليم")
