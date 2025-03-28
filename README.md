# NYC Weather Prediction API

A Flask API for predicting weather conditions in New York City using historical data (2016-2022).

## Project Structure
```
Weather_Prediction/
├── data/                   # Raw and processed datasets
│   └── NYC_Weather_2016_2022.csv
├── models/                 # Trained models
│   └── model.pkl
├── notebooks/              # Jupyter notebooks for EDA and modeling
│   └── Weather_Prediction_Project.ipynb
│── app.py                  # Flask API server
│── api_client.py           # API test client
│   
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Features
- Linear regression model trained on 6 years of NYC weather data
- REST API endpoint for predictions
- Handles 38 weather features including:
  - Precipitation, cloud cover, wind metrics
  - 24-hour temperature lags
  - Temporal features (hour, day, month, year)

## Setup

1. **Clone the repository**
   ```bash
   git clone [your-repo-url]
   cd TASK_NYW
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
