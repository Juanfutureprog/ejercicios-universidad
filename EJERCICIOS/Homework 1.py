from datetime import date

# exercise 1
def greeting():
    name = input("Enter your name:")
    if name == "":
        print("Name cannot be empty.")
    elif not name.replace(" ", "").isalpha():
        print("Name only accepts letters.")
    else:
        print(f"Hello {name}, welcome to our program!.")
greeting()


# exercise 2
def sum_numbers():
    print("Enter two numbers to perform the sum:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}.")
sum_numbers()


# exercise 3
def double_triple():
    number = float(input("Enter a number to show its double and triple:"))
    double = number * 2
    triple = number * 3
    print(f"The double of {number} is: {double} and the triple is: {triple}.")
double_triple()


# exercise 4
def rectangle_area():
    length = float(input("Enter the length of the rectangle:"))
    width = float(input("Enter the width of the rectangle:"))
    area = length * width
    print(f"The area of the rectangle is: {area}.")
rectangle_area()


# exercise 5
def temperature_conversion():
    celsius = float(input("Enter the temperature in Celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}.")
temperature_conversion()


# exercise 6
def verify_age():
    age = int(input("Enter your age:"))
    if age < 0:
        print("Age cannot be negative.")
    elif age >= 18:
        print("You are of legal age.")
    else:
        print("You are a minor.")
verify_age()


# exercise 7
def greater_number():
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    if num1 > num2:
        print(f"The greater number between {num1} and {num2} is: {num1}.")
    elif num2 > num1:
        print(f"The greater number between {num1} and {num2} is: {num2}.")
    else:
        print("The numbers entered are equal.")
greater_number()


# exercise 8
def grade_average():
    grade1 = float(input("Enter the first grade:"))
    grade2 = float(input("Enter the second grade:"))
    grade3 = float(input("Enter the third grade:"))
    average = (grade1 + grade2 + grade3) / 3
    print(f"The average of the three grades is: {average:.2f}")
grade_average()


# exercise 9
def even_odd():
    number = int(input("Enter a number:"))
    if number % 2 == 0:
        print(f"The number {number} is even.")
    else:
        print(f"The number {number} is odd.")
even_odd()


# exercise 10
def verify_number():
    number = float(input("Enter a number:"))
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number is zero.")
verify_number()


# exercise 11
def calculate_discount():
    value = float(input("Enter the purchase amount:"))
    if value < 100:
        print(f"You have a 0% discount, the amount to pay is: {value}")
    elif 100 <= value <= 150:
        final_value = (value - (value * 0.10))
        print(f"You have a 10% discount, the amount to pay is: {final_value:.2f}")
    else:
        final_value = (value - (value * 0.15))
        print(f"You have a 15% discount, the amount to pay is: {final_value:.2f}")
calculate_discount()


# exercise 12
def validate_age():
    age = int(input("Enter your age:"))
    if age < 0:
        print("The age entered is negative.")
    elif age <= 12:
        print(f"Age: {age} belongs to the child category.")
    elif 13 <= age <= 17:
        print(f"Age: {age} belongs to the youth category.")
    else:
        print(f"Age: {age} belongs to the adult category.")
validate_age()


# exercise 13
def login():
    defined_user = "Messi"
    defined_password = "Vers2005"
    user = input("Enter your username:")
    password = input("Enter your password:")
    if defined_password == password and defined_user == user:
        print("Your username and password are correct, welcome to the system.")
    elif defined_password == password or defined_user == user:
        print("Please verify your username or password.")
    else:
        print("Your username and password are incorrect.")
login()


# exercise 14
def show_menu():
    print("Welcome to our menu:")
    print("1. Greet")
    print("2. Show date")
    print("3. Motivational quote")
    print("4. Exit")

def greet_menu():
    name = input("Enter your name:")
    print(f"Hello {name}, I hope you are doing well!")

def show_date():
    today = date.today()
    print(f"Hello, today's date is: {today}")

def motivational_quote():
    print("Don't count the days, make the days count. (Muhammad Ali)")

def secondary_menu():
    while True:
        show_menu()
        option = input("Choose one of the following options:").strip()
        if option == "1":
            greet_menu()
        elif option == "2":
            show_date()
        elif option == "3":
            motivational_quote()
        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Please choose a valid option.")
secondary_menu()


# exercise 15
def leap_year():
    year = int(input("Enter a year:"))
    if year % 400 == 0:
        print(f"The year {year} is a leap year.")
    elif year % 100 == 0:
        print(f"The year {year} is not a leap year.")
    elif year % 4 == 0:
        print(f"The year {year} is a leap year.")
    else:
        print(f"The year {year} is not a leap year.")
leap_year()


# exercise 16
def calculate_numbers():
    number1 = float(input("Enter the first number:"))
    number2 = float(input("Enter the second number:"))
    number3 = float(input("Enter the third number:"))
    if number1 > number2 and number1 > number3:
        print(f"The number {number1} is the greatest.")
    elif number2 > number1 and number2 > number3:
        print(f"The number {number2} is the greatest.")
    elif number3 > number1 and number3 > number2:
        print(f"The number {number3} is the greatest.")
    else:
        print("All numbers are equal.")
calculate_numbers()


# exercise 17
def student_performance():
    grade = float(input("Enter a grade:"))
    if 9 <= grade <= 10:
        print(f"Grade: {grade} - A (Excellent)")
    elif 7 <= grade <= 8:
        print(f"Grade: {grade} - B (Good)")
    elif 5 <= grade <= 6:
        print(f"Grade: {grade} - C (Average)")
    elif 0 <= grade <= 4:
        print(f"Grade: {grade} - D (Failed)")
    else:
        print("The grade is out of range.")
student_performance()


# exercise 18
def ternary_operator():
    age = int(input("Enter your age:"))
    message = "Access granted" if age >= 18 else "Access denied"
    print(message)
ternary_operator()


# exercise 19
def numbers_for():
    for i in range(1, 11):
        print(i)
numbers_for()


# exercise 20
def accumulated_sum():
    total = 0
    while True:
        number = float(input("Enter numbers to calculate an accumulated sum (0 to stop):"))
        if number == 0:
            break
        total += number
    print(f"The total sum is: {total}")
accumulated_sum()


# exercise 21
def multiplication_table():
    number = int(input("Enter a number to show its multiplication table up to 12:"))
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")
multiplication_table()


# exercise 22
def positive_numbers_array():
    array = []
    length = int(input("Enter how many numbers you want to enter:"))
    for i in range(length):
        number = float(input("Enter a number:"))
        array.append(number)

    positive_count = 0
    for number in array:
        if number > 0:
            positive_count += 1
    print(f"The amount of positive numbers is: {positive_count}")
    for number in array:
        if number > 0:
            print(number)
positive_numbers_array()


# exercise 23
def guess_number():
    attempts = 5
    defined_number = 33
    counter = 0
    while counter < attempts:
        number = int(input("Enter a number to guess the defined number:"))
        if number > defined_number:
            print("Too high, the number is lower.")
        elif number < defined_number:
            print("The number is higher, keep trying.")
        elif number == defined_number:
            print(f"Congratulations, you guessed it! The number was: {defined_number}")
            break
        counter += 1
    else:
        print(f"You did not guess, the number was: {defined_number}")
guess_number()


# exercise 24
def calculate_average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg

def average():
    array = []
    length = int(input("Enter the amount of numbers you want to average:"))
    for i in range(length):
        number = float(input("Enter the numbers to average:"))
        array.append(number)
    result = calculate_average(array)
    print(f"The average is: {result:.2f}")
average()


# exercise 25
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def verify_prime():
    number = int(input("Enter a number:"))
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")
verify_prime()


# exercise 26
def factorial(number):
    if number == 0 or number == 1:
        return 1
    return number * factorial(number - 1)

def calculate_factorial():
    number = int(input("Enter a number:"))
    print(f"The result is: {factorial(number)}")
calculate_factorial()


# exercise 27
def add():
    print("Enter two numbers to perform the sum:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 + num2
    print(f"The sum of {num1} and {num2} is: {result}.")

def subtract():
    print("Enter two numbers to perform the subtraction:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 - num2
    print(f"The subtraction of {num1} and {num2} is: {result}.")

def multiply():
    print("Enter two numbers to perform the multiplication:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 * num2
    print(f"The multiplication of {num1} and {num2} is: {result}.")

def divide():
    print("Enter two numbers to perform the division:")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if num2 != 0:
        result = num1 / num2
        print(f"The division of {num1} and {num2} is: {result:.2f}.")
    else:
        print("Cannot divide by zero.")

def calculator_menu():
    while True:
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        option = input("Choose an option:").strip()
        if option == "1":
            add()
        elif option == "2":
            subtract()
        elif option == "3":
            multiply()
        elif option == "4":
            divide()
        elif option == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

calculator_menu()