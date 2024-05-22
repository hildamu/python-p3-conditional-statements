#!/usr/bin/env python3
def admin_login(username, password):
    if username.lower() == 'admin' and password == '12345':
        print("Access granted")
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature > 90:
        return "It's too dang hot out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    else:
        return "It's a little chilly out there!"

    
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

def calculator(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero!"
    else:
        print("Invalid operation!")
        return None



   


