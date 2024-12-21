def parse_input(filename: str):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split("\n\n")

    pairs = sections[0].split("\n")
    pairs_formatted = [tuple(map(int, pair.split("|"))) for pair in pairs]

    lines = sections[1].split("\n")
    lines = [list(map(int, line.split(","))) for line in lines]

    return pairs_formatted, lines
