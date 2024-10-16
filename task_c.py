password = list(input("Please enter a password "))

hasInt = any(char.isalnum() for char in password)
hasStr = any(char.isalpha() for char in password)

validator = hasInt and hasStr

if len(password) > 7 and validator == True:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")