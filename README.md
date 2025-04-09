# NYC Weather Prediction API

A Flask API for predicting weather conditions in New York City using historical data (2016-2022).

## Project Structure
```
Weather_Prediction/
├── data/                   # All data-related files
│   ├── NYC_Weather_2016_2022.csv          # Raw historical weather dataset
│   └── predictions/                       # Folder for model output files
│       └── test_predictions.csv           # CSV containing model predictions vs actuals
│
├── models/                 # Serialized model artifacts
│   ├── model.pkl                          # Trained machine learning model
│   └── scaler.pkl                         # Fitted StandardScaler for data normalization
│
├── notebooks/              # Experimental/analysis work
│   |── sklearn.ipynb                      # Experiments with traditional ML models (Linear, RF) using
|   └── pytorch.ipynb                      # Experiments with Neural Networks using PyTorch
│
├── app.py                  # Flask application serving predictions
├── api_client.py           # Script for testing API endpoints
│   
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation and setup instructions
```

## Features
- Weather prediction models trained on 6 years of NYC weather data
- REST API endpoint for predictions
- Explored and evaluated multiple regression models
- Handles 38 weather features including:
  - Precipitation, cloud cover, wind metrics
  - 24-hour temperature lags
  - Temporal features (hour, day, month, year, encoded cyclically)

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/armen-meliksetyan/weather-forecast-ml.git
   cd weather-forecast-ml
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API
```bash
python app.py
```
API will run at `http://localhost:5000`

### Making Predictions
Sample request:
```bash
curl -X POST http://localhost:5000/predict \
-H "Content-Type: application/json" \
-d '{
    "precipitation (mm)": 2.5,
    "rain (mm)": 1.2,
    ...
    "year": 2023
}'
```

Or use the test client:
```bash
python api_client.py
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict` | POST | Make weather predictions |

## Dependencies
- Python 3.8+
- Flask
- requests
- pandas
- scikit-learn
- numpy
- matplotlib
- seaborn
