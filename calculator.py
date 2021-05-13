from typing import Container


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def cal():
    while True:
        num1 = input("Please enter a number\n")
        print("select operation")
        print("+ add")
        print("- subtract")
        print("* multiply")
        print("/ divide")
        choice = input("Enter your action: +/ -/ */ /\n")
        if choice in ('+', '-', '*', '/'):
            num2 = input("Please enter another number\n")
            if choice == '+':
                print(num1, "+", num2, "=", round(add(float(num1), float(num2)), 2))

            elif choice == '-':
                print(num1, "-", num2, "=", round(subtract(float(num1), float(num2)), 2))

            elif choice == '*':
                print(num1, "*", num2, "=", round(multiply(float(num1), float(num2)), 2))

            elif choice == '/':
                if num2 == '0':
                    print("invalid input")
                    cal()
                print(num1, "/", num2, "=", round(divide(float(num1), float(num2)), 2))
        else:
            print("invalid input")
cal()