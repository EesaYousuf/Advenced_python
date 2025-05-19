
"""from cryptography.fernet import Fernet
import json
import os
import getpass
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)

def load_key():
    return open(KEY_FILE, "rb").read()

if not os.path.exists(KEY_FILE):
    generate_key()

fernet = Fernet(load_key())






def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)
def encrypt(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt(token):
    return fernet.decrypt(token.encode()).decode()
def add_password():
    service = input("Enter service name: ")
    username = input("Enter username/email: ")
    password = getpass.getpass("Enter password: ")

    data = load_data()
    data[service] = {
        "username": encrypt(username),
        "password": encrypt(password)
    }
    save_data(data)
    print(f"🔐 Password for '{service}' added successfully.")
def view_password():
    service = input("Enter service to retrieve: ")
    data = load_data()
    if service in data:
        username = decrypt(data[service]["username"])
        password = decrypt(data[service]["password"])
        print(f"\n🧾 Service: {service}")
        print(f"👤 Username: {username}")
        print(f"🔑 Password: {password}")
    else:
        print("❌ Service not found.")
def delete_password():
    service = input("Enter service to delete: ")
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        print(f"🗑️ Deleted '{service}' entry.")
    else:
        print("❌ Service not found.")
def main():
    print("\n🔐 Secure Password Vault 🔐")
    master_pwd = getpass.getpass("Enter Master Password: ")
    
    # You can implement a hashed check here if you want
    if master_pwd != "admin123":  # CHANGE THIS in real apps
        print("❌ Wrong password.")
        return

    while True:
        print("\n--- MENU ---")
        print("1. Add New Password")
        print("2. View Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            view_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("👋 Exiting Password Manager.")
            break
        else:
            print("❗ Invalid choice.")
if __name__ == "__main__":
    main()"""
from cryptography.fernet import Fernet
import json
import os
import getpass

# Define file paths for key and data storage
KEY_FILE = "secret.key"
DATA_FILE = "passwords.json"

def generate_key():
    """Generate a new Fernet key and save it to KEY_FILE."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as file:
        file.write(key)

def load_key():
    """Load the Fernet key from KEY_FILE."""
    return open(KEY_FILE, "rb").read()

# Generate key if it does not exist
if not os.path.exists(KEY_FILE):
    generate_key()

# Initialize Fernet object
fernet = Fernet(load_key())

def load_data():
    """Load password data from DATA_FILE."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_data(data):
    """Save password data to DATA_FILE."""
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def encrypt(text):
    """Encrypt text using Fernet."""
    return fernet.encrypt(text.encode()).decode()

def decrypt(token):
    """Decrypt text using Fernet."""
    return fernet.decrypt(token.encode()).decode()

def add_password():
    """Add a new password entry."""
    service = input("Enter service name: ")
    username = input("Enter username/email: ")
    password = getpass.getpass("Enter password: ")

    data = load_data()
    data[service] = {
        "username": encrypt(username),
        "password": encrypt(password)
    }
    save_data(data)
    print(f"🔐 Password for '{service}' added successfully.")

def view_password():
    """Retrieve and display a password entry."""
    service = input("Enter service to retrieve: ")
    data = load_data()
    if service in data:
        username = decrypt(data[service]["username"])
        password = decrypt(data[service]["password"])
        print(f"\n🧾 Service: {service}")
        print(f"👤 Username: {username}")
        print(f"🔑 Password: {password}")
    else:
        print("❌ Service not found.")

def delete_password():
    """Delete a password entry."""
    service = input("Enter service to delete: ")
    data = load_data()
    if service in data:
        del data[service]
        save_data(data)
        print(f"🗑️ Deleted '{service}' entry.")
    else:
        print("❌ Service not found.")

def main():
    print("\n🔐 Secure Password Vault 🔐")
    master_pwd = getpass.getpass("Enter Master Password: ")
    
    # Replace 'admin123' with a more secure method in production
    if master_pwd != "admin123":
        print("❌ Wrong password.")
        return

    while True:
        print("\n--- MENU ---")
        print("1. Add New Password")
        print("2. View Password")
        print("3. Delete Password")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            add_password()
        elif choice == '2':
            view_password()
        elif choice == '3':
            delete_password()
        elif choice == '4':
            print("👋 Exiting Password Manager.")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    main()
