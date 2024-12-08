"""
Author : Gabriel de Haro
Date : December 8th, 2024
Description: Solutions for Day 8 of Advent of Code 2024.
"""

import numpy as np
from itertools import combinations


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def string_to_array(content: str) -> np.array:
    """Converts the string content into a 2D numpy array."""
    lines = content.splitlines()
    return np.array([list(line) for line in lines])


def find_antennas_position(map: np.array) -> dict:
    """Finds and returns the positions of antennas in the given map as a dictionary."""
    antennas = {}
    for i in range(map.shape[0]):
        for j in range(map.shape[1]):
            char = str(map[i, j])
            if char.isalnum():
                if char not in antennas:
                    antennas[char] = []
                antennas[char].append((i, j))
    return antennas


def get_antenna_pairs(positions: list) -> list:
    """Generates and returns all unique pairs of antenna positions."""
    return list(combinations(positions, 2))


def is_within_bounds(antinode: tuple, bounds: tuple) -> bool:
    """Checks if the given antinode is within the specified bounds of the map."""
    return 0 <= antinode[0] < bounds[0] and 0 <= antinode[1] < bounds[1]


def part_one(map: np.array) -> int:
    """Calculates and returns the number of unique antinode positions."""
    antennas = find_antennas_position(map)
    bounds = map.shape
    antinode_positions = set()
    for antenna in antennas:
        positions = antennas[antenna]
        pairs = get_antenna_pairs(positions)
        for pair in pairs:
            (x1, y1), (x2, y2) = pair

            diff_x = x2 - x1
            diff_y = y2 - y1

            antinode_1 = (x1 - diff_x, y1 - diff_y)
            antinode_2 = (x2 + diff_x, y2 + diff_y)

            for _, antinode in enumerate([antinode_1, antinode_2]):
                if is_within_bounds(antinode, bounds):
                    antinode_positions.add(antinode)

    return len(antinode_positions)


def part_two(map: np.array) -> int:
    """Calculates and returns the number of unique antinode positions."""
    antennas = find_antennas_position(map)
    bounds = map.shape
    antinode_positions = set()
    for antenna in antennas:
        positions = antennas[antenna]
        pairs = get_antenna_pairs(positions)
        for pair in pairs:
            (x1, y1), (x2, y2) = pair

            antinode_positions.add((x1, y1))
            antinode_positions.add((x2, y2))

            diff_x = x2 - x1
            diff_y = y2 - y1

            antinode_1 = (x1 - diff_x, y1 - diff_y)
            antinode_2 = (x2 + diff_x, y2 + diff_y)

            for i, antinode in enumerate([antinode_1, antinode_2]):
                while is_within_bounds(antinode, bounds):
                    antinode_positions.add(antinode)
                    if i == 0:
                        antinode = (antinode[0] - diff_x, antinode[1] - diff_y)
                    elif i == 1:
                        antinode = (antinode[0] + diff_x, antinode[1] + diff_y)
    return len(antinode_positions)


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_8/input.txt")
    map = string_to_array(content)
    print(f"The result of part 1 is : {part_one(map)}")
    print(f"The result of part 2 is : {part_two(map)}")


if __name__ == "__main__":
    main()
