# String Calculator TDD Kata

## Overview

This repository contains a solution for the String Calculator TDD Kata, implemented in Python. The solution includes the implementation of the `add` function and a suite of tests written with `pytest` to ensure correctness.

## Requirements

The `add` function should:

1. **Handle Empty String**: Return 0 for an empty string.
2. **Handle Single and Multiple Numbers**: Return the sum of numbers separated by commas or new lines.
3. **Handle Custom Delimiters**: Support custom delimiters specified in the format `//[delimiter]\n[numbers]`.
4. **Ignore Large Numbers**: Numbers greater than 1000 should be ignored.
5. **Handle Negative Numbers**: Throw an exception listing all negative numbers.

## Implementation

The implementation of the `add` function and the corresponding tests follow the TDD approach:

1. **Basic Functionality**: Tests for empty strings, single numbers, and multiple numbers.
2. **Delimiter Handling**: Tests for default delimiters, custom single-character delimiters, and multiple custom delimiters.
3. **Edge Cases**: Tests for large numbers, negative numbers, and various delimiter formats.
4. **Error Handling**: Tests for negative numbers with custom delimiters and large numbers.

## Tests

The provided tests cover the following scenarios:

- **Empty String**: Verifies that an empty string returns 0.
- **Single Number**: Tests for single number inputs.
- **Multiple Numbers**: Checks the sum of multiple numbers with default delimiters.
- **New Line Delimiters**: Ensures new line characters are handled correctly.
- **Custom Delimiters**: Validates various custom delimiters, including single and multiple characters.
- **Ignore Large Numbers**: Confirms that numbers greater than 1000 are ignored.
- **Negative Numbers**: Ensures that negative numbers raise exceptions with appropriate messages.
- **Special Characters and Whitespace**: Tests delimiters with special characters and whitespace.

## Running Tests

To run the tests:

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the tests with `pytest`.

