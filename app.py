import streamlit as st
import joblib
import numpy as np

# تحميل الموديل باستخدام joblib بدل pickle
model = joblib.load('diabetes_model (7).pkl')
