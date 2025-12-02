# Research: Simple Calculator

**Feature**: Simple Calculator (001-simple-calculator)
**Date**: 2025-12-02
**Purpose**: Resolve technology choices and document architecture decisions

## Research Questions

From Technical Context, we need to resolve:
1. **Language/Version selection**
2. **Testing framework selection**

## Decision 1: Programming Language

### Context
Need to select a programming language for a simple command-line calculator with:
- Cross-platform support (Windows, Linux, macOS)
- Easy command-line input/output
- No external dependencies needed
- Simple arithmetic operations
- Easy testing

### Options Considered

| Option | Pros | Cons | Complexity |
|--------|------|------|------------|
| **Python 3.11+** | - Built-in `input()` for CLI<br>- Cross-platform<br>- No compilation needed<br>- Simple syntax<br>- Great for beginners<br>- Rich testing ecosystem (pytest) | - Requires Python runtime<br>- Slightly slower (negligible for this use case) | Low |
| **JavaScript (Node.js 18+)** | - Cross-platform<br>- `readline` built-in<br>- Wide adoption<br>- No compilation<br>- Good testing (Jest) | - Requires Node.js runtime<br>- Async patterns may be overkill | Low |
| **Go 1.21+** | - Single binary output<br>- No runtime needed<br>- Fast<br>- Cross-compile support | - More verbose for simple tasks<br>- Compilation step required<br>- Steeper learning curve | Medium |
| **Rust 1.75+** | - Memory safe<br>- Single binary<br>- Very fast | - Overkill for this project<br>- Complex for simple CLI<br>- Steep learning curve | High |

### Decision: **Python 3.11+**

### Rationale

1. **Simplicity**: Python's `input()` function makes CLI prompting trivial
2. **Readability**: Code will be clear and maintainable
3. **Cross-platform**: Works on Windows, Linux, macOS without modification
4. **No compilation**: Run directly with `python calculator.py`
5. **Testing**: pytest provides excellent testing capabilities
6. **Learning**: If this is an educational project, Python is beginner-friendly
7. **Standard library**: All needed functionality (input, output, arithmetic, error handling) is built-in

### Alternatives Rejected

- **Node.js**: Adds unnecessary complexity with readline/promises for simple prompts
- **Go**: Compilation step and verbosity not justified for this simple tool
- **Rust**: Massive overkill for basic arithmetic calculator

## Decision 2: Testing Framework

### Context
Need testing framework for Python calculator with:
- Unit testing for calculator operations
- Integration testing for full CLI flow
- Easy test execution
- Clear error messages

### Options Considered

| Option | Pros | Cons |
|--------|------|------|
| **pytest** | - Simple syntax<br>- Excellent assertions<br>- Fixtures support<br>- Industry standard<br>- Great error output | - Requires installation (pip) |
| **unittest** | - Built into Python<br>- No installation needed | - More verbose<br>- Less readable<br>- Older style |
| **doctest** | - Tests in docstrings<br>- Documentation + tests | - Limited for complex tests<br>- Not suitable for CLI testing |

### Decision: **pytest**

### Rationale

1. **Simple syntax**: Tests are easy to write and read
2. **Better assertions**: Clear failure messages (`assert result == 8`)
3. **Fixtures**: Easy to set up test data if needed
4. **Industry standard**: Most Python projects use pytest
5. **CLI testing**: Can use `subprocess` or `monkeypatch` for testing input/output

### Installation

```bash
pip install pytest
```

### Test Structure

```python
# tests/unit/test_calculator.py
def test_addition():
    assert add(5, 3) == 8

def test_division_by_zero():
    result = divide(5, 0)
    assert result == "Error: Cannot divide by zero"
```

## Decision 3: Project Structure

### Context
Need simple, clear organization for a small calculator project.

### Decision: Minimal Structure

```
src/
├── calculator.py    # Core operations (add, subtract, multiply, divide)
├── main.py          # CLI entry point and user interaction
└── validator.py     # Input validation helpers

tests/
├── unit/
│   ├── test_calculator.py    # Test arithmetic operations
│   └── test_validator.py     # Test input validation
└── integration/
    └── test_main.py          # Test full CLI flow
```

### Rationale

1. **Separation of concerns**: Calculator logic separate from CLI interaction
2. **Testability**: Each module can be tested independently
3. **Simplicity**: Only 3 source files needed
4. **Standard Python structure**: Follows Python project conventions

## Decision 4: Error Handling Strategy

### Context
Need consistent error handling for:
- Division by zero (must show exact message)
- Invalid number input
- Invalid operation input

### Decision: **Return error strings for display, raise exceptions for program errors**

### Approach

1. **Division by zero**: Return string "Error: Cannot divide by zero"
2. **Invalid input**: Catch exceptions, re-prompt user with clear message
3. **Validation**: Validate before passing to calculator functions

### Example Pattern

```python
def divide(a, b):
    """Returns result or error message string"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
```

### Rationale

1. **Exact message requirement**: Spec requires specific error message text
2. **User-friendly**: Errors are displayable strings, not exception traces
3. **Simple flow**: No complex exception handling in main logic
4. **Testable**: Easy to assert error message strings in tests

## Technology Stack Summary

| Component | Choice | Version | Reason |
|-----------|--------|---------|--------|
| **Language** | Python | 3.11+ | Simplicity, readability, cross-platform |
| **Testing** | pytest | Latest | Industry standard, excellent DX |
| **Dependencies** | None | N/A | Standard library sufficient |
| **Runtime** | CPython | 3.11+ | Default Python implementation |

## Implementation Notes

### Entry Point

```python
# src/main.py
if __name__ == "__main__":
    # Prompt for number 1
    # Prompt for number 2
    # Prompt for operation
    # Calculate and display result
```

### Calculator Operations

Each operation as a pure function:
- `add(a, b)` → returns a + b
- `subtract(a, b)` → returns a - b
- `multiply(a, b)` → returns a * b
- `divide(a, b)` → returns a / b or error message

### Input Validation

Separate validation logic:
- `is_valid_number(input)` → True/False
- `is_valid_operation(input)` → True/False
- `parse_number(input)` → float or raises ValueError

## Next Steps

1. **Phase 1**: Create data-model.md (minimal - just input/output structure)
2. **Phase 1**: Create contracts/ (CLI interface contract)
3. **Phase 1**: Create quickstart.md (how to run the calculator)
4. **Phase 2**: Generate tasks.md with implementation steps
5. **Implementation**: Follow TDD if tests requested
