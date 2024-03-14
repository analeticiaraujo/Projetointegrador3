import hashlib
import User

def hash_password(password):
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == User.User:
        pass
    else:
        print("Invalid username")
    stored_password = get_stored_password(username)

    hashed_password = hash_password(password)

    if stored_password == hashed_password:
        print("Login successful!")
    else:
        print("Invalid username or password.")

#Arrumar para acessar banco de dados
def get_stored_password(username):
    # In a real application, you would retrieve the hashed password from the database
    # For simplicity, we'll hardcode a password here
    if username == "admin":
        return "c4ca4238a0b923820dcc509a6f75849b"  # Hashed password for "password"
    else:
        return None

login()
