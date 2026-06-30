from flask import Flask, jsonify, request
import psutil
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ALFA-BRIDGE")

app = Flask(__name__)

CERBER_API_URL = "http://localhost:8360"

class CerberLocal:
    def scan_system(self):
        return {
            "local_cpu": psutil.cpu_percent(),
            "local_memory": psutil.virtual_memory().percent,
            "local_processes": len(psutil.pids())
        }

@app.route('/scan', methods=['GET'])
def scan():
    # 1. Local system scan
    cerber_local = CerberLocal()
    combined_scan = cerber_local.scan_system()

    # 2. Try to fetch from Cerber Core API
    try:
        response = requests.get(f"{CERBER_API_URL}/status", timeout=2)
        if response.status_code == 200:
            cerber_status = response.json()
            combined_scan["cerber_core"] = cerber_status
            combined_scan["status"] = "SYNCHRONIZED"
        else:
            combined_scan["status"] = "CORE_UNAVAILABLE"
    except Exception as e:
        logger.warning(f"Could not connect to Cerber Core: {e}")
        combined_scan["status"] = "LOCAL_ONLY"

    return jsonify(combined_scan)

@app.route('/process', methods=['POST'])
def process_control():
    """Proxy process control requests to Cerber Core"""
    data = request.json
    if not data or 'symbol' not in data or 'action' not in data:
        return jsonify({"error": "Missing symbol or action"}), 400

    try:
        response = requests.post(f"{CERBER_API_URL}/processes/action", json=data, timeout=5)
        return jsonify(response.json()), response.status_code
    except Exception as e:
        logger.error(f"Error communicating with Cerber Core: {e}")
        return jsonify({"error": "Cerber Core connection failed"}), 503

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ALFA-BRIDGE ONLINE"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
