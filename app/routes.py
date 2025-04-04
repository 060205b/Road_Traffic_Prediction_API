from flask import Blueprint, request, render_template
import numpy as np
import pickle
import pandas as pd

# Define Blueprint
main = Blueprint('main', __name__)

# Load the model
with open(r'Road_traffic_severity_prediction_with_webframe_work\models_pickle_file\traffic_accident_severity_model_new1.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Mapping dictionaries
age_band_mapping = {"1": 0, "2": 1, "3": 2, "4": 3}
experience_mapping = {"1-2yr": 0, "2-5yr": 1, "5-10yr": 2, "Above 10yr": 3, "Below 1yr": 4, "No Licence": 5, "Unknown": 6}
weather_mapping = {"Normal": 0, "Raining": 1, "Raining and Windy": 2, "Cloudy": 3, "Other": 4, "Windy": 5, "Snow": 6, "Unknown": 7, "Fog or mist": 8}

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    age_band = request.form['ageRange']
    driving_experience = request.form['experience']
    weather_conditions = request.form['weather']

    # Convert user inputs to numerical values
    input_data = pd.DataFrame({
        'Age_band_of_driver': [age_band_mapping[age_band]],
        'Driving_experience': [experience_mapping[driving_experience]],
        'Weather_conditions': [weather_mapping[weather_conditions]]
    })

    # Make predictions
    prediction = loaded_model.predict(input_data)
    severity_mapping = {0: "Low", 1: "Medium", 2: "High"}
    predicted_severity = severity_mapping[prediction[0]]

    return render_template('result.html', prediction=predicted_severity)
