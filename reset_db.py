import os
from database import DB_NAME, initialize_sys

def reset_database():
    print("==================================================")
    print("            itemBox DATABASE RESET               ")
    print("==================================================")
    
    # 1. Delete database file
    if os.path.exists(DB_NAME):
        try:
            os.remove(DB_NAME)
            print(f"Existing database '{DB_NAME}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting database file: {e}")
            return

    # 2. Rebuild database with initialize_sys
    initialize_sys()
    
    print("==================================================")
    print("Success! Your database has been hard reset.")
    print("==================================================\n")

if __name__ == "__main__":
    reset_database()