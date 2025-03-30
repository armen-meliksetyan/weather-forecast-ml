import requests

API_URL = "http://localhost:5000/predict"

sample_data = {
    "temperature_2m (°C)": 1.3,
    "precipitation (mm)": 0,
    "rain (mm)": 0,
    "cloudcover (%)": 0,
    "cloudcover_low (%)": 0,
    "cloudcover_mid (%)": 0,
    "cloudcover_high (%)": 0,
    "windspeed_10m (km/h)": 8.3,
    "winddirection_10m (°)": 268,
    "hour": 8,
    "day": 24,
    "month": 11,
    "year": 2017,
    "temp_lag_1": 1,
    "temp_lag_2": 1.2,
    "temp_lag_3": 1.3,
    "temp_lag_4": 1.4,
    "temp_lag_5": 1.3,
    "temp_lag_6": 1.8,
    "temp_lag_7": 2.4,
    "temp_lag_8": 2.9,
    "temp_lag_9": 3.6,
    "temp_lag_10": 4.9,
    "temp_lag_11": 6.1,
    "temp_lag_12": 6,
    "temp_lag_13": 5.6,
    "temp_lag_14": 5.2,
    "temp_lag_15": 4.4,
    "temp_lag_16": 3.5,
    "temp_lag_17": 3,
    "temp_lag_18": 1.4,
    "temp_lag_19": 0.3,
    "temp_lag_20": 0.3,
    "temp_lag_21": 0.3,
    "temp_lag_22": 0.1,
    "temp_lag_23": 1.2,
    "temp_lag_24": 1.6,
    # "target": 1.2
}

response = requests.post(API_URL, json=sample_data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.text)
