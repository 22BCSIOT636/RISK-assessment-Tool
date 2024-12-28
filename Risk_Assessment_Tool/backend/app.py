from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Dummy model for demonstration
def dummy_model(input_data):
    # Simulate risk score calculation
    return np.random.uniform(0, 100)

@app.route('/calculate', methods=['POST'])
def calculate_risk():
    data = request.get_json()
    input_data = data.get("input_data", "")
    risk_score = dummy_model(input_data)
    return jsonify({"risk_score": round(risk_score, 2)})

if __name__ == '__main__':
    app.run(debug=True)
