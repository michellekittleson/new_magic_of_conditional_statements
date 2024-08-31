# Task 1: Leap Year Checker

year = int(input("Enter the year: "))

if year % 100 == 0:
    print("False")
elif year % 4 == 0:
    print("True")
else:
    print("False")