from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
CORS(app)

model = load_model("diabetes_model.h5")

min_vals = np.array([0, 0, 0, 0, 0, 0.0, 0.078, 21])
max_vals = np.array([17, 199, 122, 99, 846, 67.1, 2.42, 81])

def manual_scale(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    scaled = (input_array - min_vals) / (max_vals - min_vals)
    return scaled

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    inputs = data.get('inputs', None)

    if inputs is None or len(inputs) != 8:
        return jsonify({'error': '8개의 입력값이 필요합니다.'}), 400

    scaled_input = manual_scale(inputs)
    prob = float(model.predict(scaled_input)[0][0])
    result = {
        'probability': prob,
        'prediction': '당뇨병' if prob > 0.5 else '비당뇨병'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
