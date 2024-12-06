"""
Author : Gabriel de Haro
Date : December 6th, 2024
Description: Solutions for Day 6 of Advent of Code 2024.
"""

import numpy as np
from collections import Counter

DIRECTIONS = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

ROTATION = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def string_to_array(content: str) -> np.array:
    """Converts the string content into a 2D numpy array."""
    lines = content.split("\n")
    return np.array([list(line) for line in lines])


def find_guard_position(map: np.array) -> tuple:
    """Finds the position of the guard on the map."""
    for i, row in enumerate(map):
        for j, cell in enumerate(row):
            if cell in "^>v<":
                return (i, j)


def find_guard_direction(map: np.array, guard_pos: tuple) -> str:
    """Returns the direction of the guard at the given position."""
    x, y = guard_pos
    return map[x, y]


def is_obstacle_in_front(map: np.array, guard_pos: tuple, guard_dir: str) -> bool:
    """Checks if there is an obstacle in front of the guard."""
    x, y = guard_pos

    if guard_dir == "^":
        next_pos = (x - 1, y)
    elif guard_dir == ">":
        next_pos = (x, y + 1)
    elif guard_dir == "v":
        next_pos = (x + 1, y)
    elif guard_dir == "<":
        next_pos = (x, y - 1)
    else:
        raise ValueError(f"Direction {guard_dir} non valide.")

    if 0 <= next_pos[0] < map.shape[0] and 0 <= next_pos[1] < map.shape[1]:
        return map[next_pos[0], next_pos[1]] == "#"
    else:
        return False


def change_guard_direction(guard_dir: str) -> str:
    """Changes the guard's direction by rotating 90° to the right."""
    return ROTATION[guard_dir]


def move_guard(map, guard_pos: tuple, guard_dir: str) -> tuple:
    """Moves the guard in the current direction and returns the new position."""
    dx, dy = DIRECTIONS[guard_dir]
    new_guard_pos = (guard_pos[0] + dx, guard_pos[1] + dy)
    if 0 <= new_guard_pos[0] < map.shape[0] and 0 <= new_guard_pos[1] < map.shape[1]:
        return new_guard_pos
    else:
        return False


def part_one(map: np.array, guard_pos: tuple) -> list:
    """Calculates the guard's path and returns distinct positions visited."""
    visited_position = [guard_pos]
    dir = find_guard_direction(map, guard_pos)
    while True:
        object_front = is_obstacle_in_front(map, guard_pos, dir)
        if not object_front:
            guard_pos = move_guard(map, guard_pos, dir)
            if not guard_pos:
                break
            visited_position.append(guard_pos)
            count = Counter(visited_position)
            if any(value >= 5 for value in count.values()):
                return False
        else:
            dir = change_guard_direction(dir)
    return list(set(visited_position))


def part_two(map: np.array, visited_position: list) -> int:
    """Calculate how many blocks the guard can lead in an infinite loop"""
    result = 0
    for coord in visited_position:
        guard_pos = find_guard_position(map)
        map_copy = map.copy()
        if map_copy[coord[0]][coord[1]] != "^":
            map_copy[coord[0]][coord[1]] = "#"
        if part_one(map_copy, guard_pos) is False:
            result += 1
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_6/input.txt")
    map = string_to_array(content)
    guard_pos = find_guard_position(map)
    part_one_res = part_one(map.copy(), guard_pos)
    print(f"The result of part 1 is : {len(part_one_res)}")
    print(f"The result of part 2 is : {part_two(map.copy(), part_one_res)}")


if __name__ == "__main__":
    main()
