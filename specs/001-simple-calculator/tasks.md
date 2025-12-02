---

description: "Task list for Simple Calculator implementation"
---

# Tasks: Simple Calculator

**Input**: Design documents from `/specs/001-simple-calculator/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Tests are NOT explicitly requested in the specification, so test tasks are omitted. If TDD is desired, tests should be added before implementation tasks.

**Organization**: Tasks are organized to deliver a complete MVP in one iteration since there is only one user story (P1).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1 for User Story 1)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below use this structure

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure

- [x] T001 Create src/ directory for source code
- [x] T002 Create tests/ directory structure with unit/ and integration/ subdirectories
- [x] T003 [P] Create requirements.txt with pytest dependency
- [x] T004 [P] Create README.md with basic project description and usage instructions

**Checkpoint**: ✅ Project structure ready for implementation

---

## Phase 2: User Story 1 - Basic Two-Number Calculation (Priority: P1) 🎯 MVP

**Goal**: Implement complete calculator with all four arithmetic operations (+, -, *, /) on two numbers, including division by zero error handling

**Independent Test**: Run `python src/main.py` and verify:
- Addition: 5 + 3 = 8
- Subtraction: 10 - 4 = 6
- Multiplication: 6 * 7 = 42
- Division: 20 / 4 = 5
- Decimal addition: 15.5 + 2.3 = 17.8
- Decimal division: 9 / 2 = 4.5
- Division by zero: 5 / 0 displays "Error: Cannot divide by zero"

### Implementation for User Story 1

- [x] T005 [P] [US1] Implement add() function in src/calculator.py
- [x] T006 [P] [US1] Implement subtract() function in src/calculator.py
- [x] T007 [P] [US1] Implement multiply() function in src/calculator.py
- [x] T008 [P] [US1] Implement divide() function in src/calculator.py with division by zero check
- [x] T009 [P] [US1] Implement get_number_input() function in src/validator.py for numeric input validation
- [x] T010 [P] [US1] Implement get_operation_input() function in src/validator.py for operation validation
- [x] T011 [US1] Implement main() function in src/main.py that prompts for inputs and displays results
- [x] T012 [US1] Add error handling for invalid number inputs with re-prompting in src/main.py
- [x] T013 [US1] Add error handling for invalid operation inputs with re-prompting in src/main.py
- [x] T014 [US1] Verify all acceptance scenarios from spec.md work correctly

**Checkpoint**: ✅ Calculator is fully functional - all four operations work, division by zero handled, input validation working

---

## Phase 3: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements and documentation

- [x] T015 [P] Update README.md with complete usage examples for all four operations
- [x] T016 [P] Add docstrings to all functions in src/calculator.py
- [x] T017 [P] Add docstrings to all functions in src/validator.py
- [x] T018 [P] Add docstrings to main() function in src/main.py
- [x] T019 Run manual verification against all acceptance scenarios in spec.md
- [x] T020 Verify exact error message format: "Error: Cannot divide by zero"

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **User Story 1 (Phase 2)**: Depends on Setup (Phase 1) completion
- **Polish (Phase 3)**: Depends on User Story 1 (Phase 2) completion

### User Story Dependencies

- **User Story 1 (P1)**: No dependencies on other stories (it's the only story)

### Within User Story 1

**Parallelizable Groups**:

1. **Calculator operations** (can implement in parallel):
   - T005: add()
   - T006: subtract()
   - T007: multiply()
   - T008: divide()

2. **Validation functions** (can implement in parallel):
   - T009: get_number_input()
   - T010: get_operation_input()

3. **Documentation** (can write in parallel after implementation):
   - T016: calculator.py docstrings
   - T017: validator.py docstrings
   - T018: main.py docstrings

**Sequential Requirements**:
- T011 (main.py) depends on T005-T010 completing (needs calculator and validator functions)
- T012-T013 (error handling) depends on T011 (extends main.py)
- T014 (verification) depends on T011-T013 (needs complete working calculator)

### Parallel Opportunities

Tasks marked [P] can run in parallel if multiple developers available:

**Phase 1 Parallel**:
- T003 (requirements.txt) || T004 (README.md)

**Phase 2 Parallel Group 1** (calculator operations):
- T005 (add) || T006 (subtract) || T007 (multiply) || T008 (divide)

**Phase 2 Parallel Group 2** (validation):
- T009 (get_number_input) || T010 (get_operation_input)

**Phase 3 Parallel** (documentation):
- T015 (README update) || T016 (calculator docstrings) || T017 (validator docstrings) || T018 (main docstrings)

---

## Parallel Example: User Story 1

### Parallel Group 1: Calculator Operations

```bash
# Developer A
Task: "Implement add() function in src/calculator.py"

# Developer B
Task: "Implement subtract() function in src/calculator.py"

# Developer C
Task: "Implement multiply() function in src/calculator.py"

# Developer D
Task: "Implement divide() function in src/calculator.py with division by zero check"
```

### Parallel Group 2: Validation

```bash
# Developer A
Task: "Implement get_number_input() function in src/validator.py"

# Developer B
Task: "Implement get_operation_input() function in src/validator.py"
```

---

## Implementation Strategy

### MVP First (Single Story)

1. Complete Phase 1: Setup
2. Complete Phase 2: User Story 1
3. **STOP and VALIDATE**: Test all acceptance scenarios manually
4. Complete Phase 3: Polish
5. Ship complete calculator

### Single-Story Delivery

Since there's only one user story (P1), the MVP IS the complete product:
1. Setup → Foundation ready
2. Implement User Story 1 → Complete calculator with all operations
3. Polish → Documentation and final touches
4. Ship → Fully functional calculator ready for users

### Solo Developer Strategy

Recommended order for solo implementation:

1. **Phase 1**: Setup (T001-T004) - ~5 minutes
2. **Calculator core** (T005-T008) - ~15 minutes
   - Implement all four operations (add, subtract, multiply, divide)
3. **Validation** (T009-T010) - ~10 minutes
   - Implement input validation for numbers and operations
4. **CLI interaction** (T011-T013) - ~20 minutes
   - Wire everything together with prompts and error handling
5. **Verify** (T014) - ~10 minutes
   - Test all acceptance scenarios
6. **Polish** (T015-T020) - ~15 minutes
   - Add documentation and final checks

**Total estimated time**: ~1.5 hours for solo developer

---

## Notes

- **Tests**: No test tasks included because tests are not explicitly requested in the specification. If TDD is desired, add test tasks before implementation tasks (T005-T010 would have corresponding test tasks T005a, T006a, etc.)
- **[P] tasks**: Different files, no dependencies - safe to parallelize
- **[US1] label**: All Phase 2 tasks belong to User Story 1
- **Exact paths**: Every task specifies the exact file path
- **Verification**: T014 checks all 7 acceptance scenarios from spec.md
- **Error message**: T020 verifies exact text "Error: Cannot divide by zero"
- **Single execution**: Program runs once, performs one calculation, then exits (no loop needed)
- **No external dependencies**: Only pytest for future testing, no runtime dependencies

---

## Acceptance Criteria (from spec.md)

User Story 1 is complete when all these scenarios pass:

1. ✅ Addition: Input (5, 3, +) → Output "8" (or "8.0")
2. ✅ Subtraction: Input (10, 4, -) → Output "6" (or "6.0")
3. ✅ Multiplication: Input (6, 7, *) → Output "42" (or "42.0")
4. ✅ Division: Input (20, 4, /) → Output "5" (or "5.0")
5. ✅ Decimal addition: Input (15.5, 2.3, +) → Output "17.8"
6. ✅ Decimal division: Input (9, 2, /) → Output "4.5"
7. ✅ Division by zero: Input (5, 0, /) → Output "Error: Cannot divide by zero"

---

## Quick Reference

**Total Tasks**: 20
**Setup Tasks**: 4 (T001-T004)
**Implementation Tasks**: 10 (T005-T014)
**Polish Tasks**: 6 (T015-T020)

**Parallel Opportunities**: 10 tasks can run in parallel (marked with [P])

**Critical Path**: T001 → T005-T010 → T011 → T012-T013 → T014 → T015-T020

**MVP Completion**: After T014 (User Story 1 verified)
