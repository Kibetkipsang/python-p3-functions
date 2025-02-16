#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")


greet('Kibet')

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")


greet_with_default()

def add(num1, num2):
    print('num 1' + 'num2')
    return num1 + num2

add(4, 6)

def halve(number):
    print(number / 2)
    return number / 2

halve(8)
