import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 허용

# 예시로 모델 로드 부분 (필요하면 실제 모델 로드 코드로 교체)
def load_model():
    # 여기에 모델 로드 코드 작성
    return "모델이 로드됨"

model = load_model()

@app.route("/")
def index():
    return "Hello from Flask on Render!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json  # 클라이언트에서 JSON 데이터 받음
        # 예: input_data = data["input"] 형태로 받음
        input_data = data.get("input")

        # 실제 예측 처리 (여기에 모델 예측 코드 넣기)
        # 예시: prediction = model.predict(input_data)
        prediction = "예측결과 예시"

        # JSON 형태로 결과 반환
        return jsonify({"prediction": prediction, "status": "success"})

    except Exception as e:
        return jsonify({"error": str(e), "status": "fail"}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
