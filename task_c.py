def passwordValidator(password):
    if len(password) < 8:
        return False

    letter = any(char.isalpha() for char in password)
    digit = any(char.isdigit() for char in password)

    return letter and digit

def main():
    password = input("Enter your password: ")

    if passwordValidator(password):
        print("Your password is valid.")
    else:
        print("Your password must contain at least 8 characters, and a mix of letters and numbers.")

if __name__ == "__main__":
    main()