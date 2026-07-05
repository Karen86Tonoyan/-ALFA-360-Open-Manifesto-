
import time
from pathlib import Path
import os

def original_log_aggregator_logic(root_path):
    log_files = list(root_path.glob("*.log"))
    total_lines = sum(1 for f in log_files for _ in open(f))
    return len(log_files), total_lines

def optimized_log_aggregator_logic(root_path):
    total_lines = 0
    log_files = list(root_path.glob("*.log"))
    for f in log_files:
        with open(f, 'rb') as fp:
            for chunk in iter(lambda: fp.read(1024 * 1024), b''):
                total_lines += chunk.count(b'\n')
    return len(log_files), total_lines

class CachedLogAggregator:
    def __init__(self):
        self.cache = {}

    def run(self, root_path):
        log_files = list(root_path.glob("*.log"))
        total_lines = 0
        for f in log_files:
            try:
                stat = f.stat()
                mtime = stat.st_mtime
                size = stat.st_size
                if f in self.cache:
                    cached_mtime, cached_size, cached_count = self.cache[f]
                    if cached_mtime == mtime and cached_size == size:
                        total_lines += cached_count
                        continue

                # Count lines
                count = 0
                with open(f, 'rb') as fp:
                    for chunk in iter(lambda: fp.read(1024 * 1024), b''):
                        count += chunk.count(b'\n')
                self.cache[f] = (mtime, size, count)
                total_lines += count
            except Exception:
                pass
        return len(log_files), total_lines

def setup_logs(root_path, num_files=15, lines_per_file=10000):
    root_path.mkdir(parents=True, exist_ok=True)
    for i in range(num_files):
        with open(root_path / f"test_{i}.log", "w") as f:
            for j in range(lines_per_file):
                f.write(f"[{j}] some log message with some content to make it realistic\n")

if __name__ == "__main__":
    root = Path("benchmark_logs")
    if not root.exists():
        print("Setting up benchmark logs...")
        setup_logs(root, num_files=20, lines_per_file=50000) # 1 million lines total

    print("--- First Run (Cold Cache) ---")

    start = time.perf_counter()
    count, total = original_log_aggregator_logic(root)
    end = time.perf_counter()
    print(f"Original: {count} files, {total} lines, time: {end - start:.4f}s")

    start = time.perf_counter()
    count, total = optimized_log_aggregator_logic(root)
    end = time.perf_counter()
    print(f"Optimized (No Cache): {count} files, {total} lines, time: {end - start:.4f}s")

    cached_agg = CachedLogAggregator()
    start = time.perf_counter()
    count, total = cached_agg.run(root)
    end = time.perf_counter()
    print(f"Cached (Cold): {count} files, {total} lines, time: {end - start:.4f}s")

    print("\n--- Second Run (Warm Cache - No changes) ---")

    start = time.perf_counter()
    count, total = original_log_aggregator_logic(root)
    end = time.perf_counter()
    print(f"Original: {count} files, {total} lines, time: {end - start:.4f}s")

    start = time.perf_counter()
    count, total = cached_agg.run(root)
    end = time.perf_counter()
    print(f"Cached (Warm): {count} files, {total} lines, time: {end - start:.4f}s")

    print("\n--- Third Run (Warm Cache - One file changed) ---")
    with open(root / "test_0.log", "a") as f:
        f.write("One more line\n")

    start = time.perf_counter()
    count, total = cached_agg.run(root)
    end = time.perf_counter()
    print(f"Cached (Partial): {count} files, {total} lines, time: {end - start:.4f}s")
