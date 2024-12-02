"""
Author : Gabriel de Haro
Date : December 2nd, 2024
Description: Solutions for Day 2 of Advent of Code 2024.
"""

import numpy as np


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def parse_reports(content: str) -> tuple[list[int], list[int]]:
    """Parses the input string into a list of lists of integers."""
    lines = content.strip().split("\n")
    return [list(map(int, item.split())) for item in lines]


def is_valid(report: list) -> bool:
    """
    Checks if a sequence is strictly increasing or decreasing with valid differences between consecutive elements.
    """
    report = np.array(report)
    diffs = np.diff(report)

    valid_diffs = (1 <= np.abs(diffs)) & (np.abs(diffs) <= 3)
    if not np.all(valid_diffs):
        return False

    is_increasing = np.all(diffs > 0)
    is_decreasing = np.all(diffs < 0)

    return is_increasing or is_decreasing


def part_one(report_list: list) -> int:
    """Counts the number of sublists where differences between elements are valid and the sequence is strictly increasing or decreasing."""
    return sum(is_valid(sublist) for sublist in report_list)


def part_two(report_list: list) -> int:
    """Counts the number of sublists where removing one element results in a valid sequence that is strictly increasing or decreasing."""
    result = 0
    for sublist in report_list:
        safe = False
        sublist_array = np.array(sublist)
        for i in range(len(sublist)):
            tmp_sublist = np.delete(sublist_array, i)
            if is_valid(tmp_sublist):
                safe = True
                break
        if safe:
            result += 1
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file("D:/Project/Advent_Of_Code_2024/day_2/input.txt")
    report_list = parse_reports(content)
    print(f"The result of part 1 is : {part_one(report_list)}")
    print(f"The result of part 2 is : {part_two(report_list)}")


if __name__ == "__main__":
    main()
