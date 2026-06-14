from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("ice-cream_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('ice-cream.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])

    prediction = float(model.predict([[temperature]])[0])

    return render_template(
        'ice-cream.html',
        prediction=round(prediction, 2),
        temperature=temperature
    )

if __name__ == '__main__':
    app.run(debug=True)