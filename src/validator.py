"""Input validation module for calculator."""


def get_number_input(prompt: str) -> float:
    """Get and validate numeric input from user.

    Args:
        prompt: The prompt message to display to the user

    Returns:
        Valid float number from user input

    Note:
        Re-prompts user until valid number is entered
    """
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation_input() -> str:
    """Get and validate operation input from user.

    Returns:
        Valid operation (+, -, *, /)

    Note:
        Re-prompts user until valid operation is entered
    """
    valid_operations = ['+', '-', '*', '/']

    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in valid_operations:
            return operation
        print("Invalid operation. Please enter +, -, *, or /.")
