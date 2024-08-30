from flask import Flask, request, jsonify

app = Flask(__name__)

# نقطة البداية
@app.route('/pin_supermarket', methods=['GET'])
def get_status():
    return jsonify({"status": "pin_supermarket API is running"})

# هنا سنضيف المزيد من نقاط النهاية (endpoints) لتفاعل النماذج الأخرى مع Pin_ai

if __name__ == '__main__':
    app.run(debug=True, port=5000)


# Endpoint للتفاعل مع نموذج pin_sales
@app.route('/pin_supermarket/interact_with_pin_sales', methods=['POST'])
def interact_with_pin_sales():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_sales
    response = {
        "message": "Interacted with pin_sales successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_inventory
@app.route('/pin_supermarket/interact_with_pin_inventory', methods=['POST'])
def interact_with_pin_inventory():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_sales
    response = {
        "message": "Interacted with pin_inventory successfully",
        "data": data
    }
    return jsonify(response)

# Endpoint للتفاعل مع نموذج pin_arcd
@app.route('/pin_supermarket/interact_with_pin_arcd', methods=['POST'])
def interact_with_pin_arcd():
    data = request.json
    # تنفيذ المنطق المطلوب للتفاعل مع pin_arcd
    response = {
        "message": "Interacted with pin_arcd successfully",
        "data": data
    }
    return jsonify(response)