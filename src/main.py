"""Main CLI entry point for the simple calculator."""

from calculator import add, subtract, multiply, divide
from validator import get_number_input, get_operation_input


def main():
    """Run the calculator CLI application.

    Prompts user for two numbers and an operation, then displays the result.
    Handles division by zero and invalid inputs with appropriate error messages.
    """
    # Get first number with validation
    num1 = get_number_input("Enter the first number: ")

    # Get second number with validation
    num2 = get_number_input("Enter the second number: ")

    # Get operation with validation
    operation = get_operation_input()

    # Perform calculation based on operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        # This should never happen due to validation, but handle it anyway
        print("Error: Invalid operation")
        return

    # Display result (either number or error message)
    if isinstance(result, str):
        # Error message (e.g., division by zero)
        print(result)
    else:
        # Numeric result
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
