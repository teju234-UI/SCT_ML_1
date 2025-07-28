from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html')  # Homepage with form

@app.route('/predict', methods=['POST'])
def predict():
    # Get data from form only
    sqft = float(request.form['sqft'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])

    # Make prediction
    prediction = model.predict([[sqft, bedrooms, bathrooms]])[0]
    prediction = round(prediction, 2)

    # Render the same page with prediction result
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)