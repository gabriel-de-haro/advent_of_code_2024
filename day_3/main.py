"""
Author : Gabriel de Haro
Date : December 3rd, 2024
Description: Solutions for Day 3 of Advent of Code 2024.
"""

import re


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def part_one(program: str) -> int:
    """Parses a string for "mul(x,y)" patterns and returns the sum of their products."""
    regex = "mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(regex, program)
    return sum(int(match.group(1)) * int(match.group(2)) for match in matches)


def part_two(program: str) -> int:
    """Parses a string for "mul(x,y)", "do()", and "don't()" patterns,
    computing the sum of enabled products based on the state toggled by "do()" and "don't()".
    """
    regex = "mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
    matches = re.finditer(regex, program)
    enable = True
    result = 0
    for match in matches:
        matched_condition = match.group(0)
        if matched_condition == "do()":
            enable = True
        elif matched_condition == "don't()":
            enable = False
        else:
            if enable:
                result += int(match.group(1)) * int(match.group(2))
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file("D:/Project/Advent_Of_Code_2024/day_3/input.txt")
    print(f"The result of part 1 is : {part_one(content)}")
    print(f"The result of part 2 is : {part_two(content)}")


if __name__ == "__main__":
    main()
