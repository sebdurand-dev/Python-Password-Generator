from generator import generate_password

print("Welcome to the Password Generator!")

try:
    passwordLen = int(input("How long would you like your password to be? (4-100): "))

    if passwordLen < 4:
        print("Password should be at least 4 characters long.")
        exit()

    elif passwordLen > 100:
        print("Password should be less than 100 characters long.")
        exit()

    else:
        password = generate_password(passwordLen)
        print("Generated password: ", password)

        with open('password.txt', 'w') as file:
           file.write(str(password))
           file.close()

        print("Password saved!")

except ValueError:
    print("Invalid input.")
    exit()
