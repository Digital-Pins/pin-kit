from flask import Flask, request, jsonify

app = Flask(__name__)

# نقطة البداية
@app.route('/pin_marketing', methods=['GET'])
def get_status():
    return jsonify({"status": "pin_marketing API is running"})

# هنا سنضيف المزيد من نقاط النهاية (endpoints) لتفاعل النماذج الأخرى مع Pin_ai

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# Endpoint للتفاعل مع نموذج pin_ai
@app.route('/pin_marketing/interact_with_pin_ai', methods=['POST'])
def interact_with_pin_ai():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_ai
    response = {
        "message": "Interacted with pin_ai successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_arcd
@app.route('/pin_marketing/interact_with_pin_arcd', methods=['POST'])
def interact_with_pin_arcd():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_arcd
    response = {
        "message": "Interacted with pin_arcd successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_PhiSNAIL
@app.route('/pin_marketing/interact_with_pin_PhiSNAIL', methods=['POST'])
def interact_with_pin_PhiSNAIL():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_PhiSNAIL
    response = {
        "message": "Interacted with pin_PhiSNAIL successfully",
        "data": data
    }
    return jsonify(response)
