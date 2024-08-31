# Task 1: Identify the Greatest

first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
third_num = float(input("Enter the third number: "))

if first_num >= second_num and first_num >= third_num:
    print(f"{first_num} is the largest number.")
elif second_num >= first_num and second_num >= third_num:
    print(f"{second_num} is the largest number.")
elif third_num >= first_num and third_num >= second_num:
    print(f"{third_num} is the largest number.")
else:
    print("Please make sure you have entered numbers.")

# Task 2: Identify the Smallest

if first_num <= second_num and first_num <= third_num:
    print(f"{first_num} is the smallest number.")
elif second_num <= first_num and second_num <= third_num:
    print(f"{second_num} is the smallest number.")
elif third_num <= first_num and third_num <= second_num:
    print(f"{third_num} is the smallest number.")
else:
    print("Please make sure you have entered numbers.")