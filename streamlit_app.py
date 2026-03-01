import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("StudySense - Student Productivity Predictor")

st.write("Enter student behavioral details to predict productivity score.")

# Inputs
study_hours = st.slider("Daily Study Hours", 0, 12, 4)
phone_usage = st.slider("Daily Phone Usage (hours)", 0, 15, 5)
sleep_duration = st.slider("Sleep Duration (hours)", 0, 12, 7)
motivation = st.slider("Motivation Score", 1, 5, 3)
focus = st.slider("Focus Score", 1, 5, 3)

# Prediction logic (temporary simple logic)
if st.button("Predict Productivity"):

    productivity = (
        study_hours * 2 +
        sleep_duration * 1.5 +
        motivation * 2 +
        focus * 2 -
        phone_usage * 1.5
    )

    productivity = round(productivity, 2)

    st.subheader("Predicted Productivity Score:")
    st.success(productivity)

    if productivity >= 20:
        st.write("High Productivity Student")
    elif productivity >= 12:
        st.write("Moderate Productivity Student")
    else:
        st.write("Low Productivity Student")

# Footer
st.write("StudySense AI App")
