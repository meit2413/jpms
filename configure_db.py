import sys
import os

def configure_database(filepath):
    with open(filepath, 'r') as file:
        content = file.read()

    content = content.replace("'username'     => ''", "'username'     => 'klpms_pms'")
    content = content.replace("'password'     => ''", "'password'     => 'O&H%fF)_8y;Xfe8g'")
    content = content.replace("'database'     => ''", "'database'     => 'klpms_pms'")

    with open(filepath, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python configure_db.py <path_to_database_php>")
        sys.exit(1)

    filepath = sys.argv[1]
    if not os.path.isfile(filepath):
        print(f"Error: File not found at '{filepath}'")
        sys.exit(1)

    configure_database(filepath)
    print(f"Database configuration updated in '{filepath}'")
