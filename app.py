import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
def load_model():
    return "모델이 로드됨"

model = load_model()

@app.route("/")
def index():
    return "Hello from Flask on Render!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        input_data = data.get("input")

        prediction = "예측결과 예시"

        return jsonify({"prediction": prediction, "status": "success"})

    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
