

import os

class ChangeDirectory:

    def __init__(self, target_dir):
        self.target_dir = target_dir
        self.original_dir = os.getcwd()

    def __enter__(self):
        os.chdir(os.getcwd()+self.target_dir)
        print(f"Switched working directory to: {os.getcwd()}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.original_dir)
        print(f"Restored original directory to: {os.getcwd()}")


# --- Usage ---
print(f"Initial Directory: {os.getcwd()}")

with ChangeDirectory("/new_directory"):
    print(f"Inside Block Directory: {os.getcwd()}")
    with open('result1.txt') as f1 :
        f1.write("This file is written while changing the working directory")

print(f"Final Directory: {os.getcwd()}")