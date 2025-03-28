from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import pickle

app = Flask(__name__)
with (
    open("models/linear_regression_model.pkl", "rb") as model_file,
    open("models/scaler.pkl", "rb") as scaler_file
):
    model = pickle.load(model_file)
    scaler = pickle.load(scaler_file)

NUMERICAL_FEATURES = ['precipitation (mm)', 'rain (mm)', 'cloudcover (%)', 
                      'cloudcover_low (%)', 'cloudcover_mid (%)', 'cloudcover_high (%)', 
                      'windspeed_10m (km/h)', 'winddirection_10m (°)'] + [f'temp_lag_{i}' for i in range(1, 25)]

FEATURE_ORDER = NUMERICAL_FEATURES + ['temperature_2m (°C)', 'hour', 'day', 'month', 'year']

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        
        for feature in FEATURE_ORDER:
            if feature not in data:
                return jsonify({"error": f"Missing field: {feature}"}), 400
        
        input_df = pd.DataFrame([data], columns=FEATURE_ORDER)

        input_df['hour_sin'] = np.sin(2 * np.pi * input_df['hour'] / 24)
        input_df['hour_cos'] = np.cos(2 * np.pi * input_df['hour'] / 24)
        input_df['month_sin'] = np.sin(2 * np.pi * (input_df['month'] - 1) / 12)
        input_df['month_cos'] = np.cos(2 * np.pi * (input_df['month'] - 1) / 12)

        input_df = input_df.drop(['hour', 'month'], axis=1)

        input_df[NUMERICAL_FEATURES] = scaler.transform(input_df[NUMERICAL_FEATURES])
        
        prediction = model.predict(input_df)
        
        return jsonify({
            "prediction": float(prediction[0])
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

