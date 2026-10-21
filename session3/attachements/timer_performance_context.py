import time


class Timer:

    def __init__(self, task_name="Task"):
        self.task_name = task_name

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"[{self.task_name}] Executed in {elapsed:.4f} seconds.")


# --- Usage ---
with Timer("Processing Heavy Loop"):
    total = sum(i * i for i in range(10_000_000))