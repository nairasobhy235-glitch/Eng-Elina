import streamlit as st
import pickle
import numpy as np
import os

# تصحيح مسار الموديل (تأكدي إنها شرطتين __ قبل وبعد file)
try:
    base_path = os.path.dirname(_file_)
    model_path = os.path.join(base_path, 'diabetes_model.sav')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except Exception as e:
    st.error("تأكدي من رفع ملف diabetes_model.sav بجانب الكود!")
    st.stop()

st.title("نظام التنبؤ بالسكري - Eng Elina")

# إنشاء 17 خانة إدخال (مقسمة لـ 3 أعمدة لشكل احترافي)
inputs = []
cols = st.columns(3)
for i in range(1, 18):
    with cols[(i-1)%3]:
        # استخدمنا keys مختلفة عشان م يحصلش تداخل
        val = st.number_input(f"الميزة {i}", value=0.0, key=f"feat_{i}")
        inputs.append(val)

if st.button("Predict (تنبؤ)"):
    # تحويل المدخلات لمصفوفة مناسبة للموديل (17 Feature)
    final_features = np.array([inputs])
    prediction = model.predict(final_features)
    
    st.divider()
    if prediction[0] == 1:
        st.error("### النتيجة: الشخص مصاب بالسكري")
    else:
        st.success("### النتيجة: الشخص سليم")
