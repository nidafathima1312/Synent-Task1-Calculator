# Synent Task 1: Simple CLI Calculator

A professional command-line interface (CLI) calculator built with Python for the Synent Technologies Internship Program.

## 📌 Project Overview
This application provides a user-friendly terminal interface for basic arithmetic calculations. It includes input validation, graceful error handling for invalid operations (e.g., division by zero, non-numeric inputs), and supports continuous calculations within a loop.

## ✨ Features
- **Core Operations**: Addition, Subtraction, Multiplication, and Division.
- **Data Types**: Full support for integer and floating-point decimal inputs.
- **Error Handling**:
  - Catches invalid non-numeric inputs using `try-except` blocks (`ValueError`).
  - Prevents crash on division by zero with safety checks.
- **Interactive CLI Loop**: Keeps the program running for multiple calculations until explicitly exited.

## 🚀 How to Run

1. **Prerequisites**: Ensure Python 3.x is installed on your machine.
2. **Execution**:
   Open your terminal in the project folder and run:
   ```bash
   python calculator.py


Example Output
   =================================
       PYTHON CALCULATOR
=================================
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

Enter your choice (1-5): 1
Enter first number: 25.5
Enter second number: 14.5
Result: 25.5 + 14.5 = 40.0