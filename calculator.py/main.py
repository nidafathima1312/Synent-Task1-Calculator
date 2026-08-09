while True:
    print("\n=================================")
    print("       PYTHON CALCULATOR")
    print("=================================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice (1-5): "))
    except ValueError:
        print("Error: Invalid input. Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Thank you for using Python Calculator. Goodbye!")
        break

    if choice in [1, 2, 3, 4]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Error: Please enter valid numerical values.")
            continue

        if choice == 1:
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif choice == 2:
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif choice == 3:
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Choice out of range. Pick 1 to 5.")