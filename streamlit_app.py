import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("StudySense - AI Behavioral Analysis and Productivity Predictor")

# Load dataset from GitHub repository
df = pd.read_excel("studysense_behavioral_dataset_1.xlsx")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Show basic dataset info
st.subheader("Dataset Information")
st.write("Total Students:", df.shape[0])
st.write("Total Features:", df.shape[1])

# User inputs
st.subheader("Enter Student Behavioral Details")

study_hours = st.slider("Daily Study Hours", 0, 12, 4)
phone_usage = st.slider("Daily Phone Usage (hours)", 0, 15, 5)
sleep_duration = st.slider("Sleep Duration (hours)", 0, 12, 7)
motivation = st.slider("Motivation Score", 1, 5, 3)
focus = st.slider("Focus Score", 1, 5, 3)

# Temporary prediction logic (until ML model integrated)
if st.button("Predict Productivity"):

    productivity = (
        study_hours * 2 +
        sleep_duration * 1.5 +
        motivation * 2 +
        focus * 2 -
        phone_usage * 1.5
    )

    productivity = round(productivity, 2)

    st.success(f"Predicted Productivity Score: {productivity}")

    if productivity >= 20:
        st.write("High Productivity Student")
    elif productivity >= 12:
        st.write("Moderate Productivity Student")
    else:
        st.write("Low Productivity Student")

# Show dataset statistics
st.subheader("Dataset Statistics")
st.write(df.describe())
