import streamlit as st
import numpy as np
import joblib

# Set page config
st.set_page_config(page_title="Traffic Predictor", page_icon="🚦", layout="wide")

# Add custom CSS for background image
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                    url('https://images.unsplash.com/photo-1449824913935-59a10b8d2000?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background-color: rgba(255, 255, 255, 0.95);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-top: 2rem;
    }
    
    .stTitle {
        color: #1f2937;
        text-align: center;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .stMarkdown {
        color: white !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
    
    .stButton > button {
        background-color: #3b82f6 !important;
        color: white !important;
        border: none !important;
        border-radius: 5px !important;
        padding: 0.5rem 1rem !important;
        font-weight: bold !important;
        font-size: 2.5rem !important;
        transition: background-color 5s !important;
    }
    
    .stButton > button:hover {
        background-color: #1d4ed8 !important;
        transform: scale(1.05) !important;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3) !important;
    }
    
    .stSuccess {
    background-color: #FF6600 !important;
    border: 2px solid #ff8c00 !important;
    border-radius: 5px !important;
    padding: 1rem !important;
    }
    
    /* Target all labels in the app */
    label {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: white !important;
        margin-bottom: 0.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
    
    /* More specific selectors for Streamlit components */
    .stNumberInput label, .stSlider label, .stSelectbox label {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
    
    /* Target by Streamlit's internal classes */
    [data-testid="stNumberInput"] label, 
    [data-testid="stSlider"] label,
    .stNumberInput > div > label,
    .stSlider > div > label {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
    
    /* Catch-all for any remaining labels */
    div[class*="stNumberInput"] label,
    div[class*="stSlider"] label {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
    
    /* Style for Time Settings heading */
    .stMarkdown h3 {
        color: white !important;
        font-weight: 900 !important;
        font-size: 2.5rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8) !important;
    }
            
            
    
</style>
""", unsafe_allow_html=True)

# Load model and scaler
rf_model = joblib.load('../models/rf_model.pkl')
scaler = joblib.load('../models/scaler.pkl')

# Traffic label map
traffic_map = {'low': 0, 'normal': 1, 'high': 2, 'heavy': 3}
reverse_traffic_map = {v: k.capitalize() for k, v in traffic_map.items()}

st.title("🚦 Traffic Situation Predictor")

st.markdown("Enter traffic data below to predict the current traffic condition.")

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    car = st.number_input("Number of Cars", min_value=0, value=50)
    bike = st.number_input("Number of Bikes", min_value=0, value=5)

with col2:
    bus = st.number_input("Number of Buses", min_value=0, value=2)
    truck = st.number_input("Number of Trucks", min_value=0, value=10)

# Time inputs
st.markdown("### ⏰ Time Settings")
col3, col4 = st.columns(2)
with col3:
    hour = st.selectbox("Hour", list(range(24)), index=8)
with col4:
    minute = st.selectbox("Minute", [0, 15, 30, 45], index=2)

time_in_mins = hour * 60 + minute

# Center the predict button
col_center = st.columns([1, 2, 1])
with col_center[1]:
    if st.button("🔮 Predict Traffic Situation", use_container_width=True):
        input_data = [[car, bike, bus, truck, time_in_mins]]
        scaled_input = scaler.transform(input_data)
        prediction = rf_model.predict(scaled_input)[0]
        label = reverse_traffic_map[prediction]
        
        # Add emoji based on traffic level
        traffic_emoji = {
            'Low': '🟢',
            'Normal': '🟡', 
            'High': '🟠',
            'Heavy': '🔴'
        }
        
        st.success(f"{traffic_emoji.get(label, '🚦')} **Predicted Traffic Situation: {label}**")