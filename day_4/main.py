"""
Author : Gabriel de Haro
Date : December 4th, 2024
Description: Solutions for Day 4 of Advent of Code 2024.
"""

import numpy as np

DIRECTIONS_XMAS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
DIRECTIONS_X_MAS = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def string_to_array(content: str) -> np.array:
    """Converts the string content into a 2D numpy array."""
    lines = content.split("\n")
    return np.array([list(line) for line in lines])


def is_xmas(array: np.array, i: int, j: int, di: int, dj: int) -> bool:
    """Checks if the sequence "M", "A", "S" appears in the specified direction."""
    sequence = ["M", "A", "S"]
    for k in range(1, 4):
        ni, nj = i + k * di, j + k * dj
        if not (0 <= ni < array.shape[0] and 0 <= nj < array.shape[1]):
            return False
        if array[ni][nj] != sequence[k - 1]:
            return False
    return True


def part_one(array: np.array) -> int:
    """Counts how many times the sequence "X", "M", "A", "S" appears in the array."""
    result = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i][j] == "X":
                for di, dj in DIRECTIONS_XMAS:
                    if is_xmas(array, i, j, di, dj):
                        result += 1
    return result


def is_x_mas(array: np.array, i: int, j: int) -> bool:
    """Checks if there is a valid pattern of "M", "A", "S" around a given "A"."""
    letters = []
    for direction in DIRECTIONS_X_MAS:
        ni, nj = i + direction[0], j + direction[1]
        if 0 <= ni < array.shape[0] and 0 <= nj < array.shape[1]:
            if array[ni][nj] == "M" or array[ni][nj] == "S":
                letters.append(array[ni][nj])
    return (
        letters.count("M") == 2
        and letters.count("S") == 2
        and letters[0] != letters[-1]
    )


def part_two(array: str) -> int:
    """Counts how many times the pattern "M", "A", "S" appears around an "A" in the array."""
    result = 0
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            if array[i][j] == "A":
                if is_x_mas(array, i, j):
                    result += 1
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file("D:/Project/Advent_Of_Code_2024/day_4/input.txt")
    array = string_to_array(content)
    print(f"The result of part 1 is : {part_one(array)}")
    print(f"The result of part 2 is : {part_two(array)}")


if __name__ == "__main__":
    main()
