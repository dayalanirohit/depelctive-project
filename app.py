#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np

# Load model
with open("knn_potability_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("💧 Water Potability Prediction using KNN (k=18)")
st.markdown("Enter the values for each water quality parameter below:")

# Input fields
ph = st.number_input("pH (0 to 14)", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
hardness = st.number_input("Hardness (mg/L)", min_value=0.0, value=150.0)
solids = st.number_input("Solids (ppm)", min_value=0.0, value=10000.0)
chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=7.0)
sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=300.0)
conductivity = st.number_input("Conductivity (μS/cm)", min_value=0.0, value=400.0)
organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=15.0)
trihalomethanes = st.number_input("Trihalomethanes (μg/L)", min_value=0.0, value=60.0)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=3.0)

# Predict button
if st.button("Predict Potability"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    
    prediction = model.predict(input_data)

    st.markdown("### 🔍 Prediction Result:")
    st.success("💧 Predicted Potability: ✅ Safe to Drink (1)" if prediction[0] == 1 else "💧 Predicted Potability: ❌ Not Safe to Drink (0)")


# In[ ]:




