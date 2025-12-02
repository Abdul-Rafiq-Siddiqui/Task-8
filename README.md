# Simple Calculator

A command-line calculator that performs basic arithmetic operations on two numbers.

## Features

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Division by zero error handling
- Input validation with helpful error messages

## Requirements

- Python 3.11 or higher

## Usage

Run the calculator:

```bash
python src/main.py
```

Follow the prompts to enter:
1. First number
2. Second number
3. Operation (+, -, *, /)

The calculator will display the result.

## Examples

### Addition
```
$ python src/main.py
Enter the first number: 5
Enter the second number: 3
Enter the operation (+, -, *, /): +
Result: 8
```

### Subtraction
```
$ python src/main.py
Enter the first number: 10
Enter the second number: 4
Enter the operation (+, -, *, /): -
Result: 6
```

### Multiplication
```
$ python src/main.py
Enter the first number: 6
Enter the second number: 7
Enter the operation (+, -, *, /): *
Result: 42
```

### Division
```
$ python src/main.py
Enter the first number: 20
Enter the second number: 4
Enter the operation (+, -, *, /): /
Result: 5.0
```

### Decimal Numbers
```
$ python src/main.py
Enter the first number: 15.5
Enter the second number: 2.3
Enter the operation (+, -, *, /): +
Result: 17.8
```

### Division by Zero
```
$ python src/main.py
Enter the first number: 5
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Cannot divide by zero
```

### Invalid Input Handling
```
$ python src/main.py
Enter the first number: abc
Invalid input. Please enter a valid number.
Enter the first number: 5
Enter the second number: 3
Enter the operation (+, -, *, /): %
Invalid operation. Please enter +, -, *, or /.
Enter the operation (+, -, *, /): +
Result: 8
```

## Development

Install development dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

## Project Structure

```
├── src/
│   ├── calculator.py   # Arithmetic operations
│   ├── validator.py    # Input validation
│   └── main.py         # CLI entry point
├── tests/
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
└── requirements.txt    # Dependencies
```
