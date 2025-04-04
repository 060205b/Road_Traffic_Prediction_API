# Road Traffic Accident Severity Prediction API (Enhanced Version)

## Overview
This project is an **enhanced version** of the Traffic Accident Severity Prediction System. It now includes a **Flask-based REST API** that allows external applications to interact with the machine learning model. This enhancement enables seamless integration of accident severity predictions into other applications.

The project includes:
- **REST API** for programmatic access to accident severity predictions.
- **Flask-based Web Application** for interactive usage.
- **Pre-trained Machine Learning Model** served via API.
- **Model Interpretation** using SHAP and LIME visualizations.

## Features
- **REST API for Predictions**: The API provides an endpoint to submit accident data and receive severity predictions.
- **Web Application**: Built using Flask for easy manual input and visualization.
- **Machine Learning Model Integration**: The pre-trained Random Forest model predicts severity levels.
- **Data Visualization**: SHAP and LIME explanations help interpret predictions.

## Project Structure
```
Road_Traffic_Prediction_API/
│
├── app/
│   ├── __init__.py           # Flask app factory
│   ├── routes.py             # Web routes (form-based prediction)
│   ├── model.py              # Machine learning model loading
│   ├── utils.py              # Helper functions
│
├── dataset/
│   ├── cleaned.csv           # Processed dataset
│   ├── RTA_Dataset.csv       # Raw dataset
│
├── models_pickle_file/
│   ├── traffic_accident_severity_model.pkl  # Saved ML model
│
├── static/
│   ├── image/
│   │   ├── lime_plot.png     # LIME explanation plot
│   │   ├── shap_plot.png     # SHAP explanation plot
│   ├── video/
│   │   ├── Index_bg_video.mp4  # Homepage background video
│   │   ├── result_bg_video.mp4 # Result page background video
│   ├── Dynamic_Filtering.js  # JavaScript for frontend interactions
│   ├── Style.css             # Stylesheet for frontend
│
├── templates/
│   ├── index.html            # Homepage with prediction form
│   ├── result.html           # Prediction result page
│
├── app.py                    # Flask app entry point
├── model.ipynb               # Jupyter Notebook for model training
├── Prediction_video.mp4       # Demo video of the application
├── README.md                  # This file
├── run.py                     # Script to run the Flask app
``` 

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/traffic-accident-severity-prediction.git
cd traffic-accident-severity-prediction
```

### 2. Set Up a Virtual Environment (Recommended)
```bash
# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application
```bash
python run.py
```
The application will be available at **http://127.0.0.1:5000/**.

## API Usage
This enhanced version introduces a **REST API** to enable programmatic access.

### **Endpoint: `/predict_api`**
#### **Request Format:**
```json
{
  "Age_band_of_driver": "18-30",
  "Driving_experience": "1-2 years",
  "Weather_conditions": "Clear",
  "Type_of_collision": "Rear collision",
  "Cause_of_accident": "Over speeding"
}
```
#### **Response Format:**
```json
{
  "Severity": "High"
}
```

## Key Enhancements
- **REST API Implementation**: Exposes an endpoint for external access.
- **Structured Project Organization**: Improved file structuring for better maintainability.
- **Machine Learning Model Deployment**: The trained model is now served as an API.
- **Frontend and Backend Integration**: The Flask application seamlessly connects to the REST API.

## Dependencies
- **Flask** (Web framework for REST API)
- **Flask-RESTful** (For creating API endpoints)
- **scikit-learn** (Machine learning model deployment)
- **Pandas** (Data handling and processing)
- **SHAP & LIME** (Model explainability tools)
- **Pickle** (Model serialization)

## Demonstration Video
- **[Prediction API Demo Video](Prediction_video.mp4)**

## License
This project is licensed under the **MIT License**.

## 📞 Contact  
For questions or support, reach out via:  
📧 **Email:** bhuvaneshwaribalaji06@gmail.com 
🐙 **GitHub:** [your-username](https://github.com/060205b)  
