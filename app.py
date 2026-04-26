
import streamlit as st
import pickle
import numpy as np
import os

# 1. إعداد مسار الموديل لضمان عدم ظهور FileNotFoundError
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model.sav')

# تحميل الموديل (تأكدي أن ملف diabetes_model.sav مرفوع بجانب هذا الملف)
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("خطأ: ملف 'diabetes_model.sav' غير موجود في المستودع. يرجى رفعه!")
    st.stop()

# 2. واجهة التطبيق
st.set_page_config(page_title="Diabetes Prediction", layout="wide")
st.title("نظام التنبؤ بمرض السكري - Eng Elina")
st.markdown("يرجى إدخال البيانات الـ 17 المطلوبة للموديل:")

# 3. تنظيم الخانات في أعمدة (17 خانة)
col1, col2, col3 = st.columns(3)
inputs = []

with col1:
    for i in range(1, 7):
        val = st.number_input(f"Feature {i}", value=0.0, key=f"f{i}")
        inputs.append(val)

with col2:
    for i in range(7, 13):
        val = st.number_input(f"Feature {i}", value=0.0, key=f"f{i}")
        inputs.append(val)

with col3:
    for i in range(13, 18):
        val = st.number_input(f"Feature {i}", value=0.0, key=f"f{i}")
        inputs.append(val)

# 4. زر التنبؤ
if st.button("Predict (تنبؤ)"):
    # تحويل المدخلات لمصفوفة (Array)
    features = np.array([inputs])
    
    # إجراء التنبؤ
    prediction = model.predict(features)
    
    st.divider()
    if prediction[0] == 1:
        st.error("### النتيجة: الشخص مصاب بالسكري (Positive)")
    else:
        st.success("### النتيجة: الشخص سليم (Negative)")

# ملاحظة: يمكنك تغيير أسماء "Feature 1, 2..." بأسماء الأعمدة الحقيقية لاحقاً.

