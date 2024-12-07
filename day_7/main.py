"""
Author : Gabriel de Haro
Date : December 7th, 2024
Description: Solutions for Day 7 of Advent of Code 2024.
"""

import re
from itertools import product


OPERATORS_1 = ["+", "*"]
OPERATORS_2 = ["+", "*", "||"]


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def get_data(content: str) -> tuple[list, list]:
    """Extracts test values and remaining numbers from the content using regex."""
    pattern = r"^(\d+):\s*(\d+(?: \d+)*)"
    matches = re.findall(pattern, content, re.MULTILINE)
    test_values = [int(match[0]) for match in matches]
    remaining_number = [list(map(int, match[1].split())) for match in matches]
    return test_values, remaining_number


def left_right_calculation(data: tuple[list, list], combination: tuple) -> int:
    """Calculates the result of an expression by applying operators from left to right."""
    result = data[0]
    for i in range(1, len(data)):
        if combination[i - 1] == "+":
            result += data[i]
        elif combination[i - 1] == "*":
            result *= data[i]
        elif combination[i - 1] == "||":
            result = int(str(result) + str(data[i]))
    return result


def part_one_and_two(data: tuple[list, list], operator: list) -> int:
    """Calculates the sum of test values that match a left-to-right calculation."""
    result = 0
    for test_value, equation in zip(data[0], data[1]):
        combinations = list(product(operator, repeat=len(equation) - 1))
        for combination in combinations:
            if test_value == left_right_calculation(equation, combination):
                result += test_value
                break
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_7/input.txt")
    data = get_data(content)
    print(f"The result of part 1 is : {part_one_and_two(data, OPERATORS_1)}")
    print(f"The result of part 2 is : {part_one_and_two(data, OPERATORS_2)}")


if __name__ == "__main__":
    main()
