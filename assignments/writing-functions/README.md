# 📘 Assignment: Writing Reusable Functions

## 🎯 Objective

Learn how to write well-organized, reusable functions with clear parameters, return values, and documentation. You'll practice breaking problems into smaller functions and writing code that other programmers can easily understand and use.

## 📝 Tasks

### 🛠️ Write Functions with Parameters and Return Values

#### Description
Write functions that accept input parameters and return meaningful results. Focus on function signatures that make the code self-documenting.

#### Requirements
Completed program should:

- Write a function `calculate_rectangle_area(length, width)` that returns the area of a rectangle
- Write a function `convert_celsius_to_fahrenheit(celsius)` that converts temperature and returns the result
- Write a function `is_positive(number)` that returns `True` if the number is positive, `False` otherwise
- Test each function with multiple inputs and print the results
- Example usage:
  ```python
  print(calculate_rectangle_area(5, 3))  # 15
  print(convert_celsius_to_fahrenheit(0))  # 32.0
  print(is_positive(-5))  # False
  ```

### 🛠️ Add Docstrings and Handle Multiple Cases

#### Description
Write functions that handle edge cases and include docstrings so other programmers understand what they do.

#### Requirements
Completed program should:

- Write a function `find_max(a, b, c)` that finds and returns the largest of three numbers, with a docstring explaining what it does
- Write a function `count_vowels(text)` that counts and returns the number of vowels in a string
- Handle edge cases (empty strings, None values if applicable)
- Include docstrings for both functions that explain parameters and return values
- Example:
  ```python
  def find_max(a, b, c):
      """Find the largest of three numbers."""
      # implementation
  ```

### 🛠️ Organize Code into Reusable Modules

#### Description
Create a small utility module with related functions that work together, practicing code organization and function composition.

#### Requirements
Completed program should:

- Write a function `calculate_circle_area(radius)` that returns the area of a circle
- Write a function `calculate_circle_circumference(radius)` that returns the circumference
- Write a helper function `validate_radius(radius)` that checks if a radius is valid (positive number)
- Use the helper function in both circle functions to ensure inputs are valid before calculating
- Demonstrate all functions working together with different inputs
