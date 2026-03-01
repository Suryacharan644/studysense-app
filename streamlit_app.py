import streamlit as st
import pandas as pd
import numpy as np

# Load dataset
df = pd.read_excel("studysense_behavioral_dataset_1.xlsx")

# Title
st.title("StudySense - AI Behavioral Productivity Predictor")

# Show dataset preview
st.subheader("Dataset Preview")
st.dataframe(df.head())

# Show dataset info
st.subheader("Dataset Overview")
st.write("Total Students:", df.shape[0])
st.write("Total Features:", df.shape[1])

# Create mapping functions for categorical ranges
def convert_study_hours(value):
    mapping = {
        "<1": 0.5,
        "1–2": 1.5,
        "2–4": 3,
        ">4": 5
    }
    return mapping.get(value, 0)

def convert_sleep_duration(value):
    mapping = {
        "<5": 4,
        "5–6": 5.5,
        "6–8": 7,
        ">8": 9
    }
    return mapping.get(value, 7)

# User inputs (matching dataset)
st.subheader("Enter Student Details")

study_hours = st.selectbox(
    "Daily Study Hours",
    ["<1", "1–2", "2–4", ">4"]
)

phone_usage = st.slider("Daily Phone Usage (hours)", 0, 15, 5)

sleep_duration = st.selectbox(
    "Sleep Duration",
    ["<5", "5–6", "6–8", ">8"]
)

motivation = st.slider("Motivation Score", 1, 5, 3)

consistency = st.slider("Consistency Score", 1, 5, 3)

energy = st.slider("Energy Level", 1, 5, 3)

procrastination = st.slider("Procrastination Level", 1, 5, 3)

# Convert inputs
study_hours_num = convert_study_hours(study_hours)
sleep_duration_num = convert_sleep_duration(sleep_duration)

# Temporary prediction logic (until ML model added)
if st.button("Predict Productivity"):

    productivity = (
        study_hours_num * 2 +
        sleep_duration_num * 1.5 +
        motivation * 2 +
        consistency * 1.5 +
        energy * 1.5 -
        phone_usage * 1.5 -
        procrastination * 2
    )

    productivity = max(1, min(5, round(productivity / 5)))

    st.success(f"Predicted Productivity Score: {productivity}")

    if productivity >= 4:
        st.write("High Productivity Student")
    elif productivity >= 3:
        st.write("Moderate Productivity Student")
    else:
        st.write("Low Productivity Student")

# Show statistics
st.subheader("Dataset Statistics")
st.write(df.describe())
