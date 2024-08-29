from flask import Flask, request, jsonify
from src.manager.PhiUSIIL import PhiUSIIL  # استيراد النموذج المناسب
import numpy as np

app = Flask(__name__)

# تهيئة نموذج PhiUSIIL
phiusiil_model = PhiUSIIL()

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json['data']
    prediction = phiusiil_model.predict(np.array(data))
    return jsonify(prediction.tolist())

@app.route('/train', methods=['POST'])
def train():
    data = request.json['data']
    labels = request.json['labels']
    phiusiil_model.train(np.array(data), np.array(labels))
    return jsonify({"status": "training_complete"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
