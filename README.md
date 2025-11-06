# Heart Disease Prediction System

A machine learning-based web application that predicts the risk of heart disease based on various medical parameters.

## 👨‍💻 Author
**Aslok Singh Rajput**  
📧 Email: aslok.rajput143@gmail.com

## 📋 Overview
This project uses machine learning to predict whether a patient has a high or low risk of heart disease based on 13 medical attributes. The application features a user-friendly web interface built with Flask and provides instant predictions.

## ✨ Features
- **Interactive Web Interface**: Easy-to-use form for inputting patient data
- **Real-time Predictions**: Instant risk assessment based on ML model
- **Responsive Design**: Modern gradient UI with smooth animations
- **Pre-trained Model**: Uses a pickled machine learning model for predictions
- **13 Medical Parameters**: Comprehensive analysis including age, blood pressure, cholesterol, and more

## 🛠️ Technologies Used
- **Backend**: Flask (Python)
- **Machine Learning**: scikit-learn
- **Data Processing**: NumPy, Pandas
- **Frontend**: HTML5, CSS3
- **Model Persistence**: Pickle
- **Deployment**: Gunicorn

## 📊 Dataset
The project uses a heart disease dataset (`heart.csv`) containing 304 patient records with the following features:

| Feature | Description | Range/Values |
|---------|-------------|--------------|
| age | Age of patient | Years |
| sex | Gender | 0 = Female, 1 = Male |
| cp | Chest pain type | 0-3 |
| trestbps | Resting blood pressure | mm Hg |
| chol | Serum cholesterol | mg/dl |
| fbs | Fasting blood sugar > 120 mg/dl | 0 = No, 1 = Yes |
| restecg | Resting ECG results | 0-2 |
| thalach | Maximum heart rate achieved | bpm |
| exang | Exercise induced angina | 0 = No, 1 = Yes |
| oldpeak | ST depression induced by exercise | Numeric |
| slope | Slope of peak exercise ST segment | 0-2 |
| ca | Number of major vessels | 0-4 |
| thal | Thalassemia | 0-3 |
| target | Heart disease diagnosis | 0 = No, 1 = Yes |

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
Open your browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure
```
Heart-Disease-Prediction/
│
├── app.py                      # Main Flask application
├── model.pkl                   # Pre-trained ML model
├── heart.csv                   # Dataset
├── hd.ipynb                    # Jupyter notebook (model training)
├── requirements.txt            # Python dependencies
├── README.md                   # Project documentation
│
├── static/
│   └── css/
│       └── main.css           # Stylesheet
│
└── templates/
    ├── index.html             # Home page with input form
    └── result.html            # Prediction result page
```

## 💻 Usage

1. **Open the application** in your web browser
2. **Fill in the form** with the patient's medical information:
   - Age
   - Sex (Male/Female)
   - Chest Pain Type (1-4)
   - Resting Blood Pressure
   - Cholesterol Level
   - Fasting Blood Sugar
   - Resting ECG Results
   - Maximum Heart Rate
   - Exercise Induced Angina
   - ST Depression
   - Slope of Peak Exercise ST Segment
   - Number of Major Vessels
   - Thalassemia Value
3. **Click "Predict"** to get the risk assessment
4. **View the result**: The system will display either "High Risk" or "Low Risk" of heart disease

## 🔍 Model Information
The machine learning model is stored in `model.pkl` and was trained on the heart disease dataset. The model takes 13 features as input and outputs a binary prediction (0 = Low Risk, 1 = High Risk).

## 📦 Dependencies
```
Flask
gunicorn
numpy
pandas
scikit-learn
scipy
seaborn
matplotlib
Flask-Cors
pydotplus
Flask-RESTful
Flask-SQLAlchemy
```

## 🎨 UI Features
- Modern gradient background (orange to red)
- Dark container with semi-transparent background
- Smooth animations and transitions
- Responsive design for all screen sizes
- Interactive hover effects on buttons and inputs

## ⚠️ Disclaimer
This application is for educational and informational purposes only. It should **NOT** be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for medical concerns.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## 📝 License
This project is open source and available for educational purposes.

## 📧 Contact
**Aslok Singh Rajput**  
Email: aslok.rajput143@gmail.com

---

⭐ If you found this project helpful, please consider giving it a star!
