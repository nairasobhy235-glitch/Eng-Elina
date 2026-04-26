
import streamlit as st
import pickle
import numpy as np

# تحميل الموديل
model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title("نظام التنبؤ بمرض السكري")

# لازم تعملي 17 مدخل لأن الموديل متدرب على كده
inputs = []
for i in range(1, 18):
    val = st.number_input(f"Feature {i}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    # تحويل المدخلات لمصفوفة مناسبة للموديل
    features = np.array([inputs])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.error("مصاب")
    else:
        st.success("غير مصاب")
