import streamlit as st
import pandas as pd
import pickle

# Title
st.title("Student Performance Prediction")

# Load data
data = pd.read_csv("AI-Data.csv")

# Show dataset (optional)
if st.checkbox("Show Dataset"):
    st.write(data)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Get user input
hours_studied = st.number_input("Hours Studied")
attendance = st.number_input("Number of Attendances")

if st.button("Predict"):
    prediction = model.predict([[hours_studied, attendance]])
    st.write("Predicted Student Outcome:", prediction[0])
