password = list(input("Please enter a password "))

validator = any(isinstance(item, (int, str)) for item in password) 

if len(password) >= 7 and validator == True:
    print("Your password is valid")
else:
    print("Your password must contain at least 8 characters, and a mix of letters and numbers")