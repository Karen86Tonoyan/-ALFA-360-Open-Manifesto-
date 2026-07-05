
import os
import threading
from pathlib import Path
from cerber_alfa360_core import CerberEngine

def test_log_aggregator_accuracy():
    test_root = Path("test_agg_accuracy")
    test_root.mkdir(parents=True, exist_ok=True)

    # Clean old logs
    for f in test_root.glob("*.log"):
        f.unlink()

    engine = CerberEngine(root_path=test_root)

    # 1. Create a log file
    log1 = test_root / "test1.log"
    log1.write_text("line1\nline2\nline3\n")

    # Manually run the logic (it's normally in a thread)
    stop_event = threading.Event()

    # We need a way to trigger one iteration or just call the logic
    # Since _run_log_aggregator is a loop, we can't easily call it once without modification
    # but we can look at the engine state after it runs once if we start it.

    # Let's mock log method to capture the output
    captured_logs = []
    def mock_log(proc, msg):
        if proc == "log_aggregator":
            captured_logs.append(msg)

    engine.log = mock_log

    # Run one iteration manually by copying the logic if needed,
    # but let's try to run the thread for a short bit.
    engine.start_process("木") # log_aggregator
    import time
    time.sleep(1) # wait for one iteration (it waits 12s, so this might be too short if it sleeps first)

    # Actually it runs immediately then waits.

    print(f"Captured: {captured_logs}")
    assert "3 total entries" in captured_logs[0]

    # 2. Update the log file
    with open(log1, "a") as f:
        f.write("line4\n")

    # Force another iteration by stopping and starting (clears thread but cache is in engine)
    engine.stop_process("木")
    captured_logs.clear()
    engine.start_process("木")
    time.sleep(1)

    print(f"Captured after update: {captured_logs}")
    assert "4 total entries" in captured_logs[0]

    # 3. Add another file
    log2 = test_root / "test2.log"
    log2.write_text("newfile_line1\n")

    engine.stop_process("木")
    captured_logs.clear()
    engine.start_process("木")
    time.sleep(1)

    print(f"Captured after new file: {captured_logs}")
    assert "5 total entries" in captured_logs[0]
    assert "2 files" in captured_logs[0]

    engine.stop_all()
    print("Accuracy test passed!")

if __name__ == "__main__":
    test_log_aggregator_accuracy()
