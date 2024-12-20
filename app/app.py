from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load model
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = data.get("features")
    if not features:
        return jsonify({"error": "Invalid input"}), 400

    prediction = model.predict([features])
    return jsonify({"prediction": prediction.tolist()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)