import streamlit as st
import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('model.sav')

# Application Title
st.title("Sales Prediction Web App")
st.write("Enter the advertising budgets below to estimate the expected sales.")

# Input fields for features
st.header("Advertising Budgets (in thousands of dollars)")
tv_budget = st.slider("TV Budget", min_value=0.0, max_value=300.0, value=150.0, step=0.1)
radio_budget = st.slider("Radio Budget", min_value=0.0, max_value=50.0, value=25.0, step=0.1)
newspaper_budget = st.slider("Newspaper Budget", min_value=0.0, max_value=120.0, value=30.0, step=0.1)

# Prepare input data matching the feature names expected by the model
input_data = pd.DataFrame({
    'TV': [tv_budget],
    'Radio': [radio_budget],
    'Newspaper': [newspaper_budget]
})

# Prediction
if st.button("Predict Sales"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Sales: **{prediction:.2f}** units")
