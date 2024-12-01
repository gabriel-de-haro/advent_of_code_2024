"""
Author : Gabriel de Haro
Date : December 1st, 2024
Description: Solutions for Day 1 of Advent of Code 2024.
"""

from collections import Counter


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def parse_columns(content: str) -> tuple[list[int], list[int]]:
    """Parses the input string into two columns of integers."""
    lines = content.strip().split("\n")
    col1, col2 = zip(*[map(int, line.split()) for line in lines])
    return list(col1), list(col2)


def part_one(col1: list, col2: list) -> int:
    """Calculates the sum of absolute differences between sorted elements of two columns."""
    col1.sort()
    col2.sort()
    return sum(abs(i - j) for i, j in zip(col1, col2))


def part_two(col1: list, col2: list) -> int:
    """Calculates the weighted sum of the elements of col1 based on their frequencies in col2."""
    col2_counts = Counter(col2)
    return sum(col2_counts[num] * num for num in col1)


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file("D:/Project/Advent_Of_Code_2024/day_1/input.txt")
    col1, col2 = parse_columns(content)
    print(f"The result of part 1 is : {part_one(col1, col2)}")
    print(f"The result of part 2 is : {part_two(col1, col2)}")


if __name__ == "__main__":
    main()
