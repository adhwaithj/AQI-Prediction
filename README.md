# AQI Prediction for KOLLAM, KARYAVATTOM, and ELOOR

## Overview

AQI Prediction is a Streamlit-based interactive web app that forecasts the Air Quality Index (AQI) for three major Kerala cities — Kollam, Karyavattom, and Eloor. The model is trained on 2023–2024 pollution data, enabling reliable and location-specific AQI forecasts based on user input.

## Key Features

* Simple and clean interface using Streamlit.
* Input fields for pollutants: PM10, PM2.5, CO, NO₂, SO₂, NH₃, and O₃.
* One-click AQI forecast using the "Predict" button.
* Dropdown menu to select city: Kollam, Karyavattom, or Eloor.
* Real-time AQI prediction displayed immediately after selection.
* Model fine-tuned with real data from 2023 and 2024 for accurate results.

## How It Works

1. Users input pollution levels.
2. On clicking "Predict", a dropdown shows three cities.
3. User picks a city.
4. The app sends inputs and city name to the trained ML model (`aqi.pkl`) for prediction.
5. The resulting AQI is shown instantly in the app.

## Technologies & Tools

* **Frontend**: Streamlit for building the web UI.
* **Backend**: Python with Pickle to load the ML model.
* **Model**: Regression-based ML model trained on 2023–2024 city-specific data.
* **Data**: Historical air quality data (PM10, PM2.5, CO, NO₂, SO₂, NH₃, O₃).
