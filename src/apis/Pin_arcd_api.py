from flask import Flask, request, jsonify

app = Flask(__name__)

# نقطة البداية
@app.route('/pin_arcd', methods=['GET'])
def get_status():
    return jsonify({"status": "Pin_arcd API is running"})

# هنا سنضيف المزيد من نقاط النهاية (endpoints) لتفاعل النماذج الأخرى مع Pin_ai

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# Endpoint للتفاعل مع نموذج pin_customer_support
@app.route('/pin_arcd/interact_with_pin_customer_support', methods=['POST'])
def interact_with_pin_customer_support():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_customer_support
    response = {
        "message": "Interacted with pin_customer_support successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_technical_support
@app.route('/pin_arcd/interact_with_pin_technical_support', methods=['POST'])
def interact_with_pin_technical_support():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_technical_support
    response = {
        "message": "Interacted with pin_technical_support successfully",
        "data": data
    }
    return jsonify(response)