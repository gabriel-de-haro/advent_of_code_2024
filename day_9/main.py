"""
Author : Gabriel de Haro
Date : December 9th, 2024
Description: Solutions for Day 9 of Advent of Code 2024.
"""


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def get_individual_blocks(content: str) -> list:
    """Generates a disk map with individual blocks based on the input string content."""
    map = []
    for i in range(len(content)):
        if i % 2 == 0:
            for _ in range(int(content[i])):
                map.append(str(i // 2))
        else:
            for _ in range(int(content[i])):
                map.append(".")
    return map


def rearrange_disk_1(map: list) -> list:
    """Rearranges the disk map by moving digits to the leftmost available positions for dots."""
    dot_list = [i for i, val in enumerate(map) if val == "."]
    num_list = [i for i, val in enumerate(map) if val.isdigit()]
    while dot_list and num_list:
        dot_index = dot_list.pop(0)
        num_index = num_list.pop()
        if dot_index < num_index:
            map[dot_index] = map[num_index]
            map[num_index] = "."
        else:
            break
    return map


def find_free_space(map: list, file_size: int) -> int:
    """Finds the first available space in the map that can accommodate a file of a given size."""
    max_index = len(map) - file_size
    for i in range(max_index + 1):
        if all(c == "." for c in map[i : i + file_size]):
            return i
    return -1


def rearrange_disk_2(map: list) -> list:
    """Rearranges the disk map by moving files (digits) to the leftmost free spaces in descending order of file IDs."""
    file_ids = sorted(set(int(c) for c in map if c.isdigit()), reverse=True)
    for file_id in file_ids:
        file_size = map.count(str(file_id))
        current_positions = [i for i, c in enumerate(map) if c == str(file_id)]
        free_space_index = find_free_space(map, file_size)
        if free_space_index != -1 and free_space_index < current_positions[0]:
            for pos in current_positions:
                map[pos] = "."
            for i in range(free_space_index, free_space_index + file_size):
                map[i] = str(file_id)
    return map


def part_one(content: str) -> int:
    """Calculates the sum of digit values multiplied by their index after rearranging the disk with the first method."""
    map = get_individual_blocks(content)
    rearranged_disk = rearrange_disk_1(map)
    return sum([int(val) * i for i, val in enumerate(rearranged_disk) if val.isdigit()])


def part_two(content: str) -> int:
    """Calculates the sum of digit values multiplied by their index after rearranging the disk with the second method."""
    map = get_individual_blocks(content)
    rearranged_disk = rearrange_disk_2(map)
    return sum([int(val) * i for i, val in enumerate(rearranged_disk) if val.isdigit()])


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_9/input.txt")
    print(f"The result of part 1 is : {part_one(content)}")
    print(f"The result of part 2 is : {part_two(content)}")


if __name__ == "__main__":
    main()
