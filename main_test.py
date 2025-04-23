# Password Generator
# Modified by Ouadia Sabih on 23/4/25

import time
import secrets
import string

version = "0.1.4v"

def get_password_length():
    while True:
        try:
            user_input = int(input("Enter the length of the password: "))
            if user_input > 0:
                return user_input
            else:
                print("Password length must be greater than 0. Defaulting to 12.")
                return 12
        except ValueError:
            print("Invalid input. Please enter an integer.")

def generate_password(length):
    characters = string.ascii_letters + string.digits + ",?§!~@><#"
    return ''.join(secrets.choice(characters) for _ in range(length))

def generate_numeric_password(length):
    return ''.join(secrets.choice(string.digits) for _ in range(length))

if __name__ == "__main__":
    password_length = get_password_length()
    password = generate_password(password_length)
    numeric_password = generate_numeric_password(password_length)

    time.sleep(1)
    print("*" * 15)
    print("Random password (string):", password)
    print("Random password (numbers):", numeric_password)