"""Quick acceptance test for calculator functions."""
import sys
sys.path.insert(0, 'src')

from calculator import add, subtract, multiply, divide

# Test scenarios from spec.md
tests = [
    (add(5, 3), 8.0, "Addition: 5 + 3"),
    (subtract(10, 4), 6.0, "Subtraction: 10 - 4"),
    (multiply(6, 7), 42.0, "Multiplication: 6 * 7"),
    (divide(20, 4), 5.0, "Division: 20 / 4"),
    (add(15.5, 2.3), 17.8, "Decimal addition: 15.5 + 2.3"),
    (divide(9, 2), 4.5, "Decimal division: 9 / 2"),
    (divide(5, 0), "Error: Cannot divide by zero", "Division by zero: 5 / 0"),
]

print("Acceptance Test Results:")
print("=" * 60)
passed = 0
failed = 0

for result, expected, description in tests:
    if result == expected:
        print(f"PASS: {description}")
        print(f"      Expected: {expected}, Got: {result}")
        passed += 1
    else:
        print(f"FAIL: {description}")
        print(f"      Expected: {expected}, Got: {result}")
        failed += 1
    print()

print("=" * 60)
print(f"Results: {passed} passed, {failed} failed")

if failed == 0:
    print("All acceptance scenarios verified successfully!")
    sys.exit(0)
else:
    print(f"ERROR: {failed} scenarios failed")
    sys.exit(1)
