try:
    grade = int(input("Enter your grade between 0 - 100 "))
    if grade >= 0 and grade <= 100:
        match grade:
            case grade if grade <= 100 and grade >= 80:
                print("Your grade is: A")
            case grade if grade <= 79 and grade >= 60:
                print("Your grade is: B")
            case grade if grade <= 59 and grade >= 50:
                print("Your grade is: C")
            case grade if grade <= 49 and grade >= 40:
                print("Your grade is: D")
            case grade if grade <= 39 or grade >= 0:
                print("Your grade is: F")
    elif grade < 0 or grade > 100:
        print("Error: Grades must be between 0 and 100")
except:
    print("Error: Please enter a number")