from flask import Flask, jsonify
import psutil

app = Flask(__name__)

class Cerber:
    def scan_system(self):
        return {
            "cpu": psutil.cpu_percent(),
            "memory": psutil.virtual_memory().percent,
            "processes": len(psutil.pids())
        }

@app.route('/scan', methods=['GET'])
def scan():
    cerber = Cerber()
    system_scan = cerber.scan_system()
    return jsonify(system_scan)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
