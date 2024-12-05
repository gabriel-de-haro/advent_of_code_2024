"""
Author : Gabriel de Haro
Date : December 5th, 2024
Description: Solutions for Day 5 of Advent of Code 2024.
"""


def read_file(filepath: str) -> str:
    """Reads the content of a file and returns it as a string."""
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def split_sections(content: str) -> tuple[dict, list]:
    """Splits the input content into rules and manuals."""
    lines = content.split("\n\n")
    sections = [line.split("\n") for line in lines]
    rules_dict = {}
    for rule in sections[0]:
        left, right = rule.split("|")
        if left not in rules_dict:
            rules_dict[left] = []
        rules_dict[left].append(right)
    manuals = [list(item.split(",")) for item in sections[1]]
    return rules_dict, manuals


def part_one(rules_dict: dict, manuals: list) -> int:
    """Calculates the sum of the middle elements of valid manuals based on the rules."""
    result = 0
    for manual in manuals:
        safe = True
        for i in range(len(manual)):
            if manual[i] in rules_dict:
                val_from_dict = rules_dict[manual[i]]
                beginning_manual = manual[:i]
                if set(beginning_manual).intersection(set(val_from_dict)):
                    safe = False
                    break
        if safe:
            result += int(manual[len(manual) // 2])
    return result


def part_two(rules_dict: dict, manuals: list) -> int:
    """Processes manuals with rule-based validation and calculates a result."""
    result = 0
    for manual in manuals:
        safe = True
        for _ in range(4):
            for elem in manual:
                if elem in rules_dict:
                    val_from_dict = rules_dict[elem]
                    beginning_manual = manual[: manual.index(elem)]
                    common_page = [
                        page for page in beginning_manual if page in val_from_dict
                    ]
                    if common_page:
                        safe = False
                        val = manual.index(elem)
                        for k in range(len(common_page)):
                            manual.remove(common_page[k])
                            manual.insert(val + k, common_page[k])
        if not safe:
            result += int(manual[len(manual) // 2])
    return result


def main() -> None:
    """Main function to read input, solve the problem, and display results."""
    content = read_file(r"D:/Project/Advent_Of_Code_2024/day_5/input.txt")
    rules_dict, manual = split_sections(content)
    print(f"The result of part 1 is : {part_one(rules_dict, manual)}")
    print(f"The result of part 2 is : {part_two(rules_dict, manual)}")


if __name__ == "__main__":
    main()
