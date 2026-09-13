# Synent Task 1: Simple CLI Calculator

A professional command-line interface (CLI) calculator built with Python for the Synent Technologies Internship Program.

## 📌 Project Overview
This application provides a user-friendly terminal interface for basic arithmetic calculations. It includes input validation, graceful error handling for invalid operations (e.g., division by zero, non-numeric inputs), and supports continuous calculations within a loop.

## 🛠️ Methodology & Logic
- **Architecture:** Structured around a `while True` loop presenting a menu driven interface to process sequential calculations.
- **Input Validation:** Uses `try-except` blocks handling `ValueError` to trap non-numeric user inputs cleanly without terminating execution.
- **Operational Logic:** Employs conditional control flows (`if-elif-else`) to route mathematical operations based on user selection.
- **Edge Case Safety:** Validates division operands before evaluation to safely handle division by zero attempts.

## ✨ Features
- **Core Operations:** Addition, Subtraction, Multiplication, and Division.
- **Data Types:** Full support for integer and floating-point decimal inputs.
- **Error Handling:** Catches invalid non-numeric inputs and prevents division-by-zero crashes.
- **Interactive CLI Loop:** Keeps the program running for multiple calculations until option `5` is selected.

## 📷 Screenshots & Execution Walkthrough

### 1. Source Code & Addition Operation
![Code and Addition](ssdivterminal.png)

### 2. Division Handling
![Division Test](screenchot-add.png)

### 3. Graceful Exit
![Exit Test](ss exit.png)

## 🚀 How to Run
- **Prerequisites:** Ensure Python 3.x is installed on your machine.
- **Execution:** Run the following command in your terminal:
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
