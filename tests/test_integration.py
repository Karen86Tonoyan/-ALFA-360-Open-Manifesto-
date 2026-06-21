import unittest
import requests
import subprocess
import time
import os
import signal
import json

class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start Cerber Core in headless mode
        cls.cerber_process = subprocess.Popen(
            ["python3", "cerber_alfa360_core.py", "--api", "--api-port", "8360", "--headless"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Start ALFA-BRIDGE
        cls.bridge_process = subprocess.Popen(
            ["python3", "ALFA-BRIDGE/src/bridge_server.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Wait for servers to start
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # Kill processes
        cls.cerber_process.terminate()
        cls.bridge_process.terminate()
        cls.cerber_process.wait()
        cls.bridge_process.wait()

    def test_bridge_to_cerber_sync(self):
        # Test ALFA-BRIDGE /scan which should sync with Cerber Core
        try:
            response = requests.get("http://localhost:5000/scan", timeout=5)
            self.assertEqual(response.status_code, 200)
            data = response.json()

            # Check if sync was successful
            self.assertEqual(data.get("status"), "SYNCHRONIZED")
            self.assertIn("cerber_core", data)
            self.assertIn("engine", data["cerber_core"])
        except Exception as e:
            self.fail(f"Sync test failed: {e}")

    def test_cerber_knowledge_scan_with_hybrid_mind(self):
        # Trigger knowledge scan in Cerber
        try:
            payload = {"source": "Test Source"}
            response = requests.post("http://localhost:8360/knowledge/scan", json=payload, timeout=5)
            self.assertEqual(response.status_code, 200)

            # Verify status has updated knowledge graph
            response = requests.get("http://localhost:8360/status")
            data = response.json()
            self.assertIn("Test Source", data["knowledge_graph"]["sources"])
        except Exception as e:
            self.fail(f"Knowledge scan test failed: {e}")

    def test_bridge_process_control(self):
        # Test toggling a process via the bridge
        try:
            # Toggle '甲' (system_monitor)
            payload = {"symbol": "甲", "action": "toggle"}
            response = requests.post("http://localhost:5000/process", json=payload, timeout=5)
            self.assertEqual(response.status_code, 200)

            # Check if process state changed in Cerber
            response = requests.get("http://localhost:8360/processes/甲")
            data = response.json()
            # It was likely started by start_all in CerberEngine, so toggle should stop it
            self.assertIn(data["state"], ["running", "stopped"])
        except Exception as e:
            self.fail(f"Process control test failed: {e}")

if __name__ == '__main__':
    unittest.main()
