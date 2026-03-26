from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

model = joblib.load("titanic_pipeline.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # DEBUG: see exactly what the browser sent
        print("FORM DATA RECEIVED:", request.form)

        # Read safely
        pclass = request.form.get('pclass')
        sex = request.form.get('sex')
        age = request.form.get('age')
        sibsp = request.form.get('sibsp')
        parch = request.form.get('parch')
        fare = request.form.get('fare')
        embarked = request.form.get('embarked')

        # Validate missing fields
        missing_fields = []
        if not pclass: missing_fields.append("pclass")
        if not sex: missing_fields.append("sex")
        if not age: missing_fields.append("age")
        if not sibsp: missing_fields.append("sibsp")
        if not parch: missing_fields.append("parch")
        if not fare: missing_fields.append("fare")
        if not embarked: missing_fields.append("embarked")

        if missing_fields:
            return render_template(
                'index.html',
                prediction_text=f"Missing fields: {', '.join(missing_fields)}"
            )

        # Convert types
        input_data = pd.DataFrame([{
            'pclass': int(pclass),
            'sex': sex,
            'age': float(age),
            'sibsp': int(sibsp),
            'parch': int(parch),
            'fare': float(fare),
            'embarked': embarked
        }])

        print("INPUT DATAFRAME:")
        print(input_data)

        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        result = "Survived" if prediction == 1 else "Did Not Survive"

        return render_template(
            'index.html',
            prediction_text=f"Prediction: {result}",
            probability_text=f"Survival Probability: {probability:.2%}"
        )

    except Exception as e:
        print("ERROR:", str(e))
        return render_template(
            'index.html',
            prediction_text=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)