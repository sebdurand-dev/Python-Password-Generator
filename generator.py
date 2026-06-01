import secrets
import string

with open('main.py', 'r') as file:
    main = file.read()

def generate_password(passwordLen):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(passwordLen))
    return password