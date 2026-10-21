from contextlib import contextmanager
import fcntl
import multiprocessing
import os
import time


@contextmanager
def file_lock(path):
    f = open(path, "a")
    print(f"[{os.getpid()}] Waiting to acquire lock...")
    fcntl.flock(f, fcntl.LOCK_EX)  # Process halts here if locked
    print(f"[{os.getpid()}] Lock ACQUIRED!")
    try:
        yield f
    finally:
        print(f"[{os.getpid()}] Releasing lock...")
        fcntl.flock(f, fcntl.LOCK_UN)
        f.close()


def worker(process_id, file_path):
    print(f"Process {process_id} starting...")
    with file_lock(file_path) as f:
        print(f"--> Process {process_id} is WRITING to file...")
        f.write(f"Process {process_id} wrote this line.\n")
        time.sleep(3)  # Hold the lock for 3 seconds to simulate heavy work
        print(f"--> Process {process_id} FINISHED writing.")


if __name__ == "__main__":
    lock_file = "demo_lock.lock"

    # Ensure clean start
    if os.path.exists(lock_file):
        os.remove(lock_file)

    # Spawn 2 concurrent processes
    p1 = multiprocessing.Process(target=worker, args=(1, lock_file))
    p2 = multiprocessing.Process(target=worker, args=(2, lock_file))

    p1.start()
    time.sleep(0.1)  # Small delay to ensure Process 1 requests the lock first
    p2.start()

    p1.join()
    p2.join()