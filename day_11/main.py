"""
Author : Gabriel de Haro
Date : December 11th, 2024
Description: Solutions for Day 11 of Advent of Code 2024.
"""

import re
from collections import Counter


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def get_data(content: str) -> list:
    """Extracts test values and remaining numbers from the content using regex."""
    pattern = r"\d+"
    matches = re.findall(pattern, content)
    return [int(match) for match in matches]


def apply_rules(counter: Counter) -> Counter:
    """Applies transformation rules to stones in the counter and returns the updated counter."""
    new_counter = Counter()
    for stone, count in counter.items():
        if stone == 0:
            new_counter[1] += count
        else:
            str_stone = str(stone)
            if len(str_stone) % 2 == 0:
                mid = len(str_stone) // 2
                left = int(str_stone[:mid])
                right = int(str_stone[mid:])
                new_counter[left] += count
                new_counter[right] += count
            else:
                new_counter[stone * 2024] += count
    return new_counter


def part_one_and_two(stones: list, nb_iter: int) -> int:
    """Simulates the transformation of stones for a given number of iterations and returns the total number of stones."""
    counter = Counter(stones)
    for _ in range(nb_iter):
        counter = apply_rules(counter)
    return sum(counter.values())


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_11/input.txt")
    print(f"The result of part 1 is : {part_one_and_two(get_data(content), 25)}")
    print(f"The result of part 2 is : {part_one_and_two(get_data(content), 75)}")


if __name__ == "__main__":
    main()
