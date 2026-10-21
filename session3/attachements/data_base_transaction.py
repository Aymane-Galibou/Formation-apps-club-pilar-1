import sqlite3

class DatabaseTransaction:

    def __init__(self, db_path):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        print("Starting transaction...")
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # An error occurred inside the block: undo all changes
            self.conn.rollback()
            print(f"Transaction failed ({exc_val}). Rolled back changes.")
        else:
            # Successful execution: commit changes
            self.conn.commit()
            print("Transaction committed successfully.")

        self.conn.close()
        return False  # Propagate the exception so caller knows it failed


# --- Usage ---
with DatabaseTransaction("app.db") as cursor:
    # cursor.execute(
    #     "CREATE TABLE IF NOT EXISTS users (id INT, name TEXT UNIQUE)"
    # )
    cursor.execute("INSERT INTO users VALUES (2, 'Mohamed')")
    # Uncommenting below triggers a duplicate primary key error:
    
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    print(data)