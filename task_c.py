password = list(input("Please enter a password "))

hasInt = any(isinstance(item, int) for item in password)
hasStr = any(isinstance(item, str) for item in password)


if len(password) >= 7 and hasInt == True and hasStr == True:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")