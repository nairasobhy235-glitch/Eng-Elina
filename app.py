import streamlit as st
import pickle
import numpy as np

st.title("Diabetes Prediction App 🩺")

# دالة لتحميل الموديل بأمان
def load_model():
    try:
        with open('diabetes_model (7).pkl', 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"خطأ في تحميل الموديل: {e}")
        return None

model = load_model()

# مدخلات البيانات
glucose = st.number_input("Glucose Level", value=100)
bmi = st.number_input("BMI", value=25.0)
age = st.number_input("Age", value=30)

if st.button("Predict"):
    if model:
        features = np.array([[glucose, bmi, age]])
        prediction = model.predict(features)
        if prediction[0] == 1:
            st.error("النتيجة: إيجابي (Positive)")
        else:
            st.success("النتيجة: سلبي (Negative)")
    else:
        st.warning("لا يمكن التوقع لأن الموديل لم يتم تحميله.")
