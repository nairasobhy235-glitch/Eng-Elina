import streamlit as st
import pickle
import numpy as np
import os

# السطر ده هو اللي كان عامل المشكلة (لازم شرطتين __ قبل وبعد file)
base_path = os.path.dirname(_file_)
model_path = os.path.join(base_path, 'diabetes_model.sav')

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("ملف diabetes_model.sav مش موجود! ارفعيه على GitHub في نفس الفولدر.")
    st.stop()

st.title("نظام التنبؤ بالسكري - Eng Elina")

# إنشاء 17 خانة إجبارية عشان الموديل يشتغل
inputs = []
cols = st.columns(3)
for i in range(1, 18):
    with cols[(i-1)%3]:
        val = st.number_input(f"Feature {i}", value=0.0, key=f"in_{i}")
        inputs.append(val)

if st.button("Predict"):
    prediction = model.predict(np.array([inputs]))
    if prediction[0] == 1:
        st.error("مصاب")
    else:
        st.success("سليم")
