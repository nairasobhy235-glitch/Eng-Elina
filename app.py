import streamlit as st
import joblib
import pickle
import numpy as np

# وظيفة لتحميل الموديل بأي طريقة ممكنة
def load_model():
    try:
        return joblib.load('diabetes_model (7).pkl')
    except:
        with open('diabetes_model (7).pkl', 'rb') as f:
            return pickle.load(f)

# تحميل الموديل
try:
    model = load_model()
except Exception as e:
    st.error(f"مشكلة في ملف الموديل: {e}")

st.set_page_config(page_title="نظام التنبؤ بالسكري", page_icon="🩺")
st.title("🩺 نظام التنبؤ بمرض السكري - Eng Elina")

# إنشاء الخانات (8 خانات بالظبط)
col1, col2 = st.columns(2)
with col1:
    v1 = st.number_input("Pregnancies", 0, 20, 0)
    v2 = st.number_input("Glucose", 0, 200, 100)
    v3 = st.number_input("Blood Pressure", 0, 150, 70)
    v4 = st.number_input("Skin Thickness", 0, 100, 20)
with col2:
    v5 = st.number_input("Insulin", 0, 900, 79)
    v6 = st.number_input("BMI", 0.0, 70.0, 25.0)
    v7 = st.number_input("Pedigree Function", 0.0, 3.0, 0.47)
    v8 = st.number_input("Age", 1, 120, 30)

if st.button("Predict (تنبؤ)"):
    # تجهيز البيانات
    features = np.array([[v1, v2, v3, v4, v5, v6, v7, v8]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("⚠️ النتيجة: إيجابي (هناك خطر إصابة)")
    else:
        st.success("✅ النتيجة: سلبي (لا يوجد خطر إصابة)")
