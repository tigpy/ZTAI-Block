import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS
from web3 import Web3
import json
import joblib

# ✅ Only ONE app declaration
app = Flask(__name__)

# ✅ Apply CORS properly
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:3001"}})


# Blockchain Setup
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7545"))

with open("../blockchain/AccessLogger.abi.json") as f:
    abi = json.load(f)

contract_address = Web3.to_checksum_address("0xbea3fbb6a971ef07be73dafb07380e00224149ab")
contract = w3.eth.contract(address=contract_address, abi=abi)
account = w3.eth.accounts[0]

# ML Model
model = joblib.load('../ai_model/model.pkl')

@app.route('/')
def home():
    return 'ZTAI-Block Backend Running'

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight success"}), 200
    print("🚨 Predict endpoint HIT!")
    try:
        data = request.get_json()
        print("📥 Received Data:", data)

        login_count = int(data.get('login_count'))
        previous_failures = int(data.get('previous_failures'))

        input_data = [[login_count, previous_failures]]
        prediction = model.predict(input_data)
        risk_score = int(prediction[0])

        print("✅ Risk Score:", risk_score)
        return jsonify({'risk_score': risk_score})
    except Exception as e:
        print("🔥 ERROR in /predict:", str(e))
        return jsonify({'error': str(e)}), 500

@app.route('/log_access', methods=['POST', 'OPTIONS'])
def log_access():
    if request.method == 'OPTIONS':
        return jsonify({"message": "CORS preflight success"}), 200
    try:
        data = request.get_json()
        print("📥 Logging Access:", data)

        user_id = data.get('user_id')
        risk_score = data.get('risk_score')

        print(f"✅ Log entry: {user_id} | Risk: {risk_score}")

        return jsonify({"message": "Logged successfully."}), 200
    except Exception as e:
        print("❌ Error in log_access:", str(e))
        return jsonify({"error": "Failed to log access"}), 500

@app.route('/get_logs', methods=['GET'])
def get_logs():
    event_filter = contract.events.AccessEvent.createFilter(fromBlock=0)
    events = event_filter.get_all_entries()
    logs = []
    for e in events:
        logs.append({
            'user': e['args']['user'],
            'action': e['args']['action'],
            'timestamp': e['args']['timestamp']
        })
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(debug=True)
