from flask import Flask, render_template, request
import numpy as np
import pickle

# Load your pre-trained model
model_path = 'model.pkl'  # Ensure your model is saved as model.pkl
loaded_model = pickle.load(open(model_path, 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def predict():
    try:
        # Retrieve form data — same column order as CSV:
        # age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal
        age      = float(request.form['age'])
        sex      = int(request.form['sex'])           # 1 = Male, 0 = Female
        cp       = int(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol     = float(request.form['chol'])
        fbs      = int(request.form['fbs'])
        restecg  = int(request.form['restecg'])
        thalach  = float(request.form['thalach'])
        exang    = int(request.form['exang'])
        oldpeak  = float(request.form['oldpeak'])     # accepts decimal values
        slope    = int(request.form['slope'])
        ca       = int(request.form['ca'])
        thal     = int(request.form['thal'])

        # Prepare input in exact CSV column order
        input_data = np.array([
            age, sex, cp, trestbps, chol, fbs,
            restecg, thalach, exang, oldpeak, slope, ca, thal
        ]).reshape(1, -1)

        prediction = loaded_model.predict(input_data)

        if prediction == 1:
            result = "High Risk of Heart Disease"
        else:
            result = "Low Risk of Heart Disease"

        return render_template('result.html', result=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
