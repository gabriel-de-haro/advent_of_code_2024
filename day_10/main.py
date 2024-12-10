"""
Author : Gabriel de Haro
Date : December 10th, 2024
Description: Solutions for Day 10 of Advent of Code 2024.
"""

import numpy as np
from typing import Union


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def string_to_array(content: str) -> np.array:
    """Converts the string content into a 2D numpy array."""
    lines = content.splitlines()
    arr = np.array([list(line) for line in lines])
    return [[int(val) for val in row] for row in arr]


def dfs(row: int, col: int, map: np.array, visited: set, part: str) -> Union[int, set]:
    """Recursively explores valid paths and counts reachable '9' or returns set of reachable '9' positions based on the part parameter."""
    rows, cols = len(map), len(map[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    if map[row][col] == 9:
        if part == "1":
            return {(row, col)}
        if part == "2":
            return 1

    count = 0
    reachable_nines = set()

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if map[nr][nc] == map[row][col] + 1:
                visited.add((nr, nc))
                result = dfs(nr, nc, map, visited, part)
                visited.remove((nr, nc))

                if part == "1":
                    reachable_nines.update(result)
                if part == "2":
                    count += result

    if part == "1":
        return reachable_nines
    if part == "2":
        return count


def part_one_and_two(map: np.array, part: str) -> int:
    """Calculates the total result by calling dfs for each trailhead based on the specified part ('1' or '2')"""
    rows, cols = len(map), len(map[0])
    total_result = 0

    for r in range(rows):
        for c in range(cols):
            if map[r][c] == 0:
                visited = {(r, c)}
                result = dfs(r, c, map, visited, part)

                if part == "1":
                    total_result += len(result)
                if part == "2":
                    total_result += result

    return total_result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_10/input.txt")
    map = string_to_array(content)
    print(f"The result of part 1 is : {part_one_and_two(map, '1')}")
    print(f"The result of part 2 is : {part_one_and_two(map, '2')}")


if __name__ == "__main__":
    main()
