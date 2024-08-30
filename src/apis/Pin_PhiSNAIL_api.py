from flask import Flask, request, jsonify

app = Flask(__name__)

# نقطة البداية
@app.route('/pin_PhiSNAIL', methods=['GET'])
def get_status():
    return jsonify({"status": "pin_PhiSNAIL API is running"})

# هنا سنضيف المزيد من نقاط النهاية (endpoints) لتفاعل النماذج الأخرى مع Pin_ai

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Endpoint للتفاعل مع نموذج pin_supermarket
@app.route('/pin_PhiSNAIL/interact_with_pin_supermarket', methods=['POST'])
def interact_with_pin_supermarket():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_supermarket
    response = {
        "message": "Interacted with pin_supermarket successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_arcd
@app.route('/pin_PhiSNAIL/interact_with_pin_arcd', methods=['POST'])
def interact_with_pin_arcd():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_arcd
    response = {
        "message": "Interacted with pin_arcd successfully",
        "data": data
    }
    return jsonify(response)