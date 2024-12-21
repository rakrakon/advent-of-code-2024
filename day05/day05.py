from typing import Tuple, List

from day05_input_parser import parse_input


def main():
    pairs, lines = parse_input("input.txt")
    print(get_result_p1(lines, pairs))
    print(get_result_p2(lines, pairs))


def get_result_p1(lines, pairs):
    result = 0
    for index, line in enumerate(lines):
        if is_line_valid(line, pairs):
            result += get_middle_number_of_line(line)
    return result


def get_middle_number_of_line(line) -> int:
    return line[len(line) // 2]


def get_rules(number: int, pairs):
    rules: List[Tuple[int, int]] = []

    for pair in pairs:
        if pair[0] == number:
            rules.append(pair)
    return rules


def is_line_valid(line, pairs):
    for index, number in enumerate(line):
        rules = get_rules(number, pairs)
        for rule in rules:
            if appears_before(rule, index, line):
                return False
    return True


def appears_before(rule, index, line) -> bool:
    for number in line[:index]:
        if number == rule[1]:
            return True
    return False


def get_result_p2(lines, pairs):
    result = 0
    for index, line in enumerate(lines):
        if not is_line_valid(line, pairs):
            while not is_line_valid(line, pairs):
                correct_line(line, pairs)
            result += get_middle_number_of_line(line)

    return result


def correct_line(line, pairs):
    for index, number in enumerate(line):
        rules = get_rules(number, pairs)
        for rule in rules:
            correct_based_on_rule(rule, index, line)


def correct_based_on_rule(rule, index, line):
    for number in line[:index]:
        if number == rule[1]:
            swap_number(rule, line)


def swap_number(rule, line):
    index1, index2 = line.index(rule[0]), line.index(rule[1])
    line[index1], line[index2] = line[index2], line[index1]


if __name__ == "__main__":
    main()
