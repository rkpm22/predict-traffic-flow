# Quick Start Guide

## 🚀 Running the Traffic Flow Prediction App

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Steps

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Web Application**
   ```bash
   cd src
   streamlit run app.py
   ```

3. **Access the Application**
   Open your browser and go to: `http://localhost:8501`

### Using the App

1. **Enter Vehicle Data:**
   - Cars: Number of cars (e.g., 50)
   - Bikes: Number of bikes (e.g., 5)
   - Buses: Number of buses (e.g., 2)
   - Trucks: Number of trucks (e.g., 10)

2. **Set Time:**
   - Hour: 0-23 (e.g., 8 for 8 AM)
   - Minute: 0, 15, 30, or 45

3. **Get Prediction:**
   Click "🔮 Predict Traffic Situation" to see results

### Example Predictions
- **🟢 Low**: Few vehicles, off-peak hours
- **🟡 Normal**: Moderate traffic, regular hours
- **🟠 High**: Heavy traffic, rush hours
- **🔴 Heavy**: Extreme congestion, peak times

### Troubleshooting

- **ModuleNotFoundError**: Install missing packages with `pip install <package_name>`
- **File not found**: Make sure you're running from the correct directory
- **Port already in use**: Use `streamlit run app.py --server.port 8502` to use a different port

### Analyzing Data

To explore the dataset and model training process:
```bash
jupyter notebook notebooks/Predict-traffic-flow.ipynb
``` 