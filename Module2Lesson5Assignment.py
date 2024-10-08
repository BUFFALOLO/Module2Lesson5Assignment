""""
1. The Calculator App
Objective: The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

Task 1: Create functions for each arithmetic operation.

Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

Task 3: Ensure your code can handle division by zero and other potential errors. 
So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

def addition():
    return num1 + num2

def subtraction():
    return num1 - num2

def multiplication():
    return num1 * num2

def division():
    if num1 == 0:
        print("Cannot divide by 0")
    elif num2 ==0:
        print("Cannot divide by 0")
    else:
        return num1 / num2

while True:
    math_type = input("Enter what math type you would like to perform or enter exit to stop (addition, subtraction, multiplication or division): ")
    if math_type == "exit":
        break
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter you second number: "))

    if math_type == "addition":
        result = addition()
        print(f"{num1} + {num2} = {result}")
    elif math_type == "subtraction":
        result = subtraction()
        print(f"{num1} - {num2} = {result}")
    elif math_type == "multiplication":
        result = multiplication()
        print(f"{num1} * {num2} = {result}")
    elif math_type == "division":
        result = division()
        print(f"{num1} / {num2} = {result}")
    else:
        print("Please enter a correct math type")
"""

"""
2. The Shopping List Maker
Objective: The aim of this assignment is to create a program that helps users make a shopping list.

Task 1: Write a function that lets the user add items to a list.

Task 2: Include a function to remove items from the list.

Task 3: Add a function that prints out the entire list in a formatted way.

Note: The goal of this is to be a program. The recommendation is to use a while loop that will allow the user to continue to add, remove, 
and print off their shopping list until they decide to "quit", also known as breaking the loop.
"""
shopping_list = []

def manage_shopping_list():
    while True:
        print("1. View Shopping List")
        print("2. Add Item to Shopping List")
        print("3. Remove Item from Shopping List")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nShopping List")
            for item in shopping_list:
                print(f"• {item}")
        elif choice == "2":
            add_item = input("Enter an item to add to the shopping list: ")
            shopping_list.append(add_item)
        elif choice == "3":
            print(shopping_list)
            remove_item = input("Enter an item you want to remove from the shopping list: ")
            shopping_list.remove(remove_item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid choice.")

manage_shopping_list()





