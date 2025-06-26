# from flask import Flask, request

# app = Flask(__name__)

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     print("🚨 Alert received:", data)
#     # You can now log, notify, act based on the alert
#     return '', 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# from flask import Flask, request, render_template, jsonify
# from datetime import datetime

# app = Flask(__name__)

# alerts = []

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     data['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     alerts.append(data)
#     return jsonify({"status": "received"}), 200

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/alerts')
# def get_alerts():
#     return jsonify(alerts)

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, request, render_template, jsonify
# from datetime import datetime

# app = Flask(__name__)
# alerts = []

# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json
#     print("Received data:", data)

#     # Extract the actual result dictionary from Splunk payload
#     result = data.get("result", {})

#     alert = {
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#         "id": result.get("id", "-"),
#         "age": result.get("age", "-"),
#         "gender": result.get("gender", "-"),
#         "hypertension": result.get("hypertension", "0"),
#         "heart_disease": result.get("heart_disease", "0"),
#         "bmi": result.get("bmi", "-"),
#         "smoking_status": result.get("smoking_status", "-"),
#         "stroke": int(result.get("stroke", 0)),
#         "recommendation": "Refer to Cardiologist" if str(result.get("stroke", "0")) == "1" else "Normal Physician Consultation Required"
#     }

#     alerts.append(alert)
#     return jsonify({"status": "received"}), 200


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/alerts')
# def get_alerts():
#     return jsonify(alerts)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)
alerts = []

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received data:", data)

    # Extract the actual result dictionary from Splunk payload
    result = data.get("result", {})

    alert = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "id": result.get("id", "-"),
        "age": result.get("age", "-"),
        "gender": result.get("gender", "-"),
        "hypertension": result.get("hypertension", "0"),
        "heart_disease": result.get("heart_disease", "0"),
        "bmi": result.get("bmi", "-"),
        "smoking_status": result.get("smoking_status", "-"),
        "stroke": int(result.get("stroke", 0)),
        "recommendation": (
            "Refer to Cardiologist" if str(result.get("stroke", "0")) == "1"
            else "Normal Physician Consultation Required"
        )
    }

    alerts.append(alert)
    return jsonify({"status": "received"}), 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/alerts')
def get_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    app.run(debug=True)
