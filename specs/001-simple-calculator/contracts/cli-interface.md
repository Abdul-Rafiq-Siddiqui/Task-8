# CLI Interface Contract: Simple Calculator

**Feature**: Simple Calculator (001-simple-calculator)
**Date**: 2025-12-02
**Interface Type**: Command Line Interface (stdin/stdout)

## Overview

This document defines the command-line interface contract for the simple calculator. It specifies the exact prompts, input format, output format, and error messages.

## Execution

### Command

```bash
python src/main.py
```

### Prerequisites

- Python 3.11 or higher installed
- No additional dependencies required for runtime

## Interface Flow

### 1. Start Program

**Action**: User runs the calculator

```bash
$ python src/main.py
```

### 2. First Number Prompt

**Prompt**: `"Enter the first number: "`

**Expected Input**: Numeric value (integer or decimal, positive or negative)

**Valid Examples**:
- `5` → Accepted as 5.0
- `3.14` → Accepted as 3.14
- `-10` → Accepted as -10.0
- `0` → Accepted as 0.0

**Invalid Input Handling**:
```
Enter the first number: abc
Invalid input. Please enter a valid number.
Enter the first number:
```

**Behavior**: Re-prompt until valid number received

### 3. Second Number Prompt

**Prompt**: `"Enter the second number: "`

**Expected Input**: Numeric value (integer or decimal, positive or negative)

**Valid Examples**: Same as first number

**Invalid Input Handling**: Same as first number (re-prompt with error message)

### 4. Operation Prompt

**Prompt**: `"Enter the operation (+, -, *, /): "`

**Expected Input**: Exactly one of: `+`, `-`, `*`, `/`

**Valid Examples**:
- `+` → Addition
- `-` → Subtraction
- `*` → Multiplication
- `/` → Division

**Invalid Input Handling**:
```
Enter the operation (+, -, *, /): %
Invalid operation. Please enter +, -, *, or /.
Enter the operation (+, -, *, /):
```

**Behavior**: Re-prompt until valid operation received

### 5. Result Display

**Format**: Direct numeric result or error message

**Success Cases**:
```
Result: 8.0
```

**Error Cases**:
```
Error: Cannot divide by zero
```

### 6. Program Exit

**Behavior**: Program terminates after displaying result

**Exit Code**:
- `0` for successful calculation
- `0` for division by zero error (expected behavior, not a program failure)

## Complete Examples

### Example 1: Addition

```
$ python src/main.py
Enter the first number: 5
Enter the second number: 3
Enter the operation (+, -, *, /): +
Result: 8.0
```

### Example 2: Subtraction

```
$ python src/main.py
Enter the first number: 10
Enter the second number: 4
Enter the operation (+, -, *, /): -
Result: 6.0
```

### Example 3: Multiplication

```
$ python src/main.py
Enter the first number: 6
Enter the second number: 7
Enter the operation (+, -, *, /): *
Result: 42.0
```

### Example 4: Division

```
$ python src/main.py
Enter the first number: 20
Enter the second number: 4
Enter the operation (+, -, *, /): /
Result: 5.0
```

### Example 5: Division with Decimal Result

```
$ python src/main.py
Enter the first number: 9
Enter the second number: 2
Enter the operation (+, -, *, /): /
Result: 4.5
```

### Example 6: Division by Zero (Error Case)

```
$ python src/main.py
Enter the first number: 5
Enter the second number: 0
Enter the operation (+, -, *, /): /
Error: Cannot divide by zero
```

### Example 7: Invalid Number Input

```
$ python src/main.py
Enter the first number: abc
Invalid input. Please enter a valid number.
Enter the first number: 5
Enter the second number: 3
Enter the operation (+, -, *, /): +
Result: 8.0
```

### Example 8: Invalid Operation Input

```
$ python src/main.py
Enter the first number: 5
Enter the second number: 3
Enter the operation (+, -, *, /): %
Invalid operation. Please enter +, -, *, or /.
Enter the operation (+, -, *, /): +
Result: 8.0
```

### Example 9: Negative Numbers

```
$ python src/main.py
Enter the first number: -5
Enter the second number: 3
Enter the operation (+, -, *, /): +
Result: -2.0
```

### Example 10: Decimal Numbers

```
$ python src/main.py
Enter the first number: 15.5
Enter the second number: 2.3
Enter the operation (+, -, *, /): +
Result: 17.8
```

## Message Catalog

### Prompts

| Prompt ID | Text | Context |
|-----------|------|---------|
| PROMPT_NUM1 | `"Enter the first number: "` | First number input |
| PROMPT_NUM2 | `"Enter the second number: "` | Second number input |
| PROMPT_OP | `"Enter the operation (+, -, *, /): "` | Operation selection |

### Results

| Result ID | Text Template | Context |
|-----------|---------------|---------|
| RESULT_SUCCESS | `"Result: {value}"` | Successful calculation |
| RESULT_DIV_ZERO | `"Error: Cannot divide by zero"` | Division by zero attempted |

### Error Messages

| Error ID | Text | Context | Recovery |
|----------|------|---------|----------|
| ERR_INVALID_NUM | `"Invalid input. Please enter a valid number."` | Non-numeric input for number | Re-prompt |
| ERR_INVALID_OP | `"Invalid operation. Please enter +, -, *, or /."` | Invalid operation character | Re-prompt |

## Input Validation Rules

### Number Input

**Rule**: Must be convertible to Python `float`

**Valid Patterns**:
- Integer: `5`, `-10`, `0`
- Decimal: `3.14`, `-2.5`, `0.0`
- Scientific notation: `1e5`, `-3.2e-2` (bonus if supported)

**Invalid Patterns**:
- Empty string: `""`
- Non-numeric: `"abc"`, `"five"`
- Multiple decimals: `"5.3.2"`
- Invalid characters: `"5a"`, `"$10"`

### Operation Input

**Rule**: Must be exactly one of the four characters: `+`, `-`, `*`, `/`

**Valid Values**: `+`, `-`, `*`, `/`

**Invalid Values**: Any other string

**Case Sensitivity**: Exact match required (no variations)

## Output Format

### Numeric Results

**Format**: `Result: {value}`

**Value Format**:
- Python default float representation
- No forced decimal places
- Shows decimals when necessary (e.g., `4.5`)
- No decimals for whole numbers (e.g., `8.0` is acceptable)

**Examples**:
- `Result: 8.0`
- `Result: 4.5`
- `Result: -2.0`

### Error Results

**Format**: Error message only (no "Result:" prefix)

**Division by Zero**:
```
Error: Cannot divide by zero
```

**Critical**: The exact text "Error: Cannot divide by zero" must be used (no variations)

## Exit Behavior

**Normal Execution**:
1. Display result
2. Exit with code 0

**No Looping**: Calculator does not ask "Do you want to calculate again?" - it exits after one calculation

**No Menu**: Calculator does not present a menu - it follows the fixed sequence (num1, num2, operation, result)

## Testing Contract

### Unit Test Expectations

Tests should verify:
- Each arithmetic operation produces correct results
- Division by zero returns the exact error message
- Input validation catches invalid numbers
- Input validation catches invalid operations

### Integration Test Expectations

Tests should verify:
- Complete flow from prompts through result display
- Error handling and re-prompting behavior
- Exact text of prompts and error messages
- Program exits after displaying result

### Test Data

See data-model.md for validation rules and test cases

## Non-Requirements

**Out of Scope**:
- No GUI
- No web interface
- No REST API
- No calculation history
- No memory functions (M+, MR, etc.)
- No advanced operations (sqrt, pow, etc.)
- No parentheses or order of operations
- No multiple operations in one input
- No "clear" or "reset" commands
- No configuration files
- No logging (unless for debugging)

## Compatibility

**Platform**: Cross-platform (Windows, Linux, macOS)
**Terminal**: Any standard terminal/command prompt
**Character Encoding**: UTF-8 (for prompts and output)
**Locale**: Decimal point character is `.` (period) - no comma support for European locales needed

## Summary

The CLI interface is intentionally simple:
- Three prompts (number, number, operation)
- One result or error message
- Clear validation with re-prompting
- Exact error message for division by zero
- No additional features or complexity
