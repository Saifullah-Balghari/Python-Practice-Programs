marks = int(input("Enter Your marks in Percentage : "))

if 0 <= marks <= 32:
    print("Remarks = 'Serius Hardwork Is Needed!' ")
    print("Grade = F ")
elif 33 <= marks <= 49:
    print("Remarks = 'Bad!' ")
    print("Grade = E ")
elif 50 <= marks <= 59:
    print("Remarks = 'Not Bad!' ")
    print("Grade = D ")
elif 60 <= marks <= 69:
    print("Remarks = Okay!")
    print("Grade = C")
elif 70 <= marks <= 79:
    print("Remarks = Good!")
    print("Grade = B")
elif 80 <= marks <= 89:
    print("Remarks = Very Good!")
    print("Grade = A")
elif 90 <= marks <= 100:
    print("Remarks = Excellent!")
    print("Grade = A+")
elif marks < 0 or marks > 100:
    print("Percentage can't be in a Negative numbers or higher then 100.")
else:
    print("Invalid input!")
