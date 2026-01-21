import numpy as np
from flask import Flask, request, render_template
import joblib
import os

app = Flask(__name__)

# Load the trained model
# Using os.path to make it robust for any OS/Deployment
base_dir = os.path.abspath(os.path.dirname(__file__))
model_path = os.path.join(base_dir, 'model', 'titanic_survival_model.pkl')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form
        # Order MUST match the training order: ['Pclass', 'Sex', 'Age', 'Fare', 'SibSp']
        features = [
            int(request.form['Pclass']),
            int(request.form['Sex']),
            float(request.form['Age']),
            float(request.form['Fare']),
            int(request.form['SibSp'])
        ]

        # Convert to numpy array
        final_features = [np.array(features)]
        
        # Predict
        prediction = model.predict(final_features)
        
        # Determine output text and CSS class
        if prediction[0] == 1:
            text = "Result: PASSENGER SURVIVED! 🎉"
            css_class = "survived"
        else:
            text = "Result: DID NOT SURVIVE 💀"
            css_class = "died"
            
        return render_template('index.html', prediction_text=text, result_class=css_class)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", result_class="died")

if __name__ == "__main__":
    app.run(debug=True)