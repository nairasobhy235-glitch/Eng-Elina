
  import streamlit as st
import pickle
import numpy as np
import os

# 1. إعداد المسار (تأكدي إنها شرطتين __ قبل وبعد كلمة file)
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model.sav')

# تحميل الموديل
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("ملف diabetes_model.sav مش موجود في الفولدر! ارفعيه بجانب ملف app.py")
    st.stop()

st.title("نظام التنبؤ بمرض السكري - Eng Elina")

# 2. إنشاء الـ 17 خانة (مقسمة لـ 3 أعمدة عشان الشكل)
inputs = []
cols = st.columns(3)

# مسميات الأعمدة بناءً على مشروعك (تقدري تعدلي الأسامي براحتك)
for i in range(1, 18):
    with cols[(i-1)%3]:
        val = st.number_input(f"الميزة (Feature) {i}", value=0.0, key=f"input_{i}")
        inputs.append(val)

# 3. تنفيذ التنبؤ
if st.button("Predict (تنبؤ)"):
    # تحويل لـ مصفوفة
    final_features = np.array([inputs])
    
    # التنبؤ
    prediction = model.predict(final_features)
    
    st.divider()
    if prediction[0] == 1:
        st.error("### النتيجة: الشخص مصاب بالسكري")
    else:
        st.success("### النتيجة: الشخص سليم")
