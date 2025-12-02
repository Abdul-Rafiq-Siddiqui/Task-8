# Data Model: Simple Calculator

**Feature**: Simple Calculator (001-simple-calculator)
**Date**: 2025-12-02
**Purpose**: Define data structures and their relationships

## Overview

This calculator has minimal data modeling needs since it:
- Performs one calculation per execution
- Does not persist state
- Does not have complex data relationships

The data model describes the in-memory structures during a single execution.

## Core Entities

### 1. CalculationInput

Represents the user's input for a single calculation.

**Attributes**:
- `number1`: float - First operand
- `number2`: float - Second operand
- `operation`: str - One of: '+', '-', '*', '/'

**Validation Rules**:
- `number1` and `number2` must be valid numeric values (integer or decimal)
- `number1` and `number2` can be positive, negative, or zero
- `operation` must be exactly one of the four allowed values: '+', '-', '*', '/'
- Any other operation value is invalid

**Example**:
```python
{
    "number1": 5.0,
    "number2": 3.0,
    "operation": "+"
}
```

### 2. CalculationResult

Represents the output of a calculation operation.

**Attributes**:
- `value`: float | str - Either the numeric result or an error message
- `is_error`: bool - True if value is an error message, False if numeric result

**Validation Rules**:
- If `is_error` is False, `value` must be a float
- If `is_error` is True, `value` must be a string
- For division by zero, `value` must be exactly: "Error: Cannot divide by zero"

**Examples**:
```python
# Success case
{
    "value": 8.0,
    "is_error": False
}

# Error case
{
    "value": "Error: Cannot divide by zero",
    "is_error": True
}
```

## Operation Definitions

### Addition (+)

**Formula**: `result = number1 + number2`

**Properties**:
- Always returns a numeric result
- No error conditions
- Supports negative numbers
- Supports decimals

### Subtraction (-)

**Formula**: `result = number1 - number2`

**Properties**:
- Always returns a numeric result
- No error conditions
- Supports negative numbers
- Supports decimals

### Multiplication (*)

**Formula**: `result = number1 * number2`

**Properties**:
- Always returns a numeric result
- No error conditions
- Supports negative numbers
- Supports decimals
- Multiplication by zero returns zero

### Division (/)

**Formula**: `result = number1 / number2`

**Properties**:
- Returns numeric result when `number2 != 0`
- Returns error message when `number2 == 0`
- Supports negative numbers
- Supports decimals
- May return non-integer result (e.g., 9 / 2 = 4.5)

**Error Condition**:
- When `number2 == 0`, return: "Error: Cannot divide by zero"

## Data Flow

```
User Input (stdin)
    ↓
Parse & Validate
    ↓
CalculationInput {number1, number2, operation}
    ↓
Execute Operation
    ↓
CalculationResult {value, is_error}
    ↓
Format & Display (stdout)
```

## State Diagram

```
[Start] → [Prompt for Number 1] → [Validate Number 1]
                                         ↓
                                    [Prompt for Number 2] → [Validate Number 2]
                                                                  ↓
                                                             [Prompt for Operation] → [Validate Operation]
                                                                                            ↓
                                                                                       [Execute Calculation]
                                                                                            ↓
                                                                                       [Display Result]
                                                                                            ↓
                                                                                         [End]
```

## Validation Logic

### Number Validation

**Input**: String from user
**Output**: float or ValidationError

**Algorithm**:
1. Strip whitespace from input
2. Attempt to convert to float
3. If successful, return float value
4. If failed, return validation error

**Valid Examples**:
- "5" → 5.0
- "3.14" → 3.14
- "-10" → -10.0
- "0" → 0.0

**Invalid Examples**:
- "abc" → ValidationError
- "" (empty) → ValidationError
- "5.3.2" → ValidationError

### Operation Validation

**Input**: String from user
**Output**: str (validated operation) or ValidationError

**Algorithm**:
1. Strip whitespace from input
2. Check if input is exactly one of: '+', '-', '*', '/'
3. If yes, return the operation
4. If no, return validation error

**Valid Examples**:
- "+" → "+"
- "-" → "-"
- "*" → "*"
- "/" → "/"

**Invalid Examples**:
- "add" → ValidationError
- "%" → ValidationError
- "x" → ValidationError
- "" (empty) → ValidationError

## Error Handling

### Division by Zero

**Condition**: `operation == '/' AND number2 == 0`

**Response**: Return exactly "Error: Cannot divide by zero"

**Example**:
```python
Input: {number1: 5.0, number2: 0.0, operation: '/'}
Output: {value: "Error: Cannot divide by zero", is_error: True}
```

### Invalid Input

**Condition**: User enters non-numeric value or invalid operation

**Response**: Re-prompt user with helpful message

**Example**:
```
Enter first number: abc
Invalid input. Please enter a valid number.
Enter first number: 5
```

## Type System

### Python Types

```python
# Input types
Number1 = float
Number2 = float
Operation = Literal['+', '-', '*', '/']

# Output types
NumericResult = float
ErrorResult = str
Result = NumericResult | ErrorResult

# Function signatures
def add(a: float, b: float) -> float
def subtract(a: float, b: float) -> float
def multiply(a: float, b: float) -> float
def divide(a: float, b: float) -> float | str  # Returns error string for division by zero
```

## Persistence

**No persistence required**. All data is:
- Input: Read from stdin during execution
- Processing: Held in memory during calculation
- Output: Written to stdout, then discarded
- No files, databases, or state preservation between executions

## Summary

The data model is intentionally minimal:
- Two input numbers (floats)
- One operation (string from limited set)
- One result (float or error string)
- No complex relationships or state management
- Validation at input boundaries
- Clear error handling for division by zero
