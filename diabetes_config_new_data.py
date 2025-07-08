import numpy as np
from tensorflow.keras.models import load_model

model = load_model("diabetes_model.h5")

min_vals = np.array([0, 0, 0, 0, 0, 0.0, 0.078, 21])
max_vals = np.array([17, 199, 122, 99, 846, 67.1, 2.42, 81])

def manual_scale(input_data):
    input_array = np.array(input_data).reshape(1, -1)
    scaled = (input_array - min_vals) / (max_vals - min_vals)
    return scaled

def predict_diabetes_manual(input_data):
    input_scaled = manual_scale(input_data)
    prob = model.predict(input_scaled)[0][0]
    print(f"당뇨병일 확률: {prob:.4f}")
    print("예측 결과:", "당뇨병" if prob > 0.5 else "비당뇨병")





predict_diabetes_manual([1, 89, 66, 23, 94, 28.1, 0.167, 21])