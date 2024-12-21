XMAS = 'XMAS'

'''
Check forward when came X
XMAS
'''
def check_next_in_row(line: str, idx: int) -> bool:
    return line[idx:4+idx] == XMAS

'''
Check when came to X then going backwards
SAMX
'''
def check_before_in_row(line: str, idx: int) -> bool:
    return line[idx-3:idx+1] == XMAS[::-1]


'''
.X..
.M..
.A..
.S..
'''
def check_below(lines, line_idx, idx) -> bool:
    for i in range(4):
        if XMAS[i] != lines[line_idx+i][idx]:
            return False

    return True

'''
.S..
.A..
.M..
.X..
'''
def check_above(lines, line_idx, idx) -> bool:
    for i in range(4):
        if XMAS[i] != lines[line_idx-i][idx]:
            return False

    return True


'''
X...
.M..
..A.
...S
'''
def check_right_diagonal_below(lines, line_idx, idx):
    for i in range(4):
        if XMAS[i] != lines[line_idx+i][idx+i]:
            return False
    return True

'''
...X
..M.
.A..
S...
'''
def check_left_diagonal_below(lines, line_idx, idx):
    for i in range(4):
        if XMAS[i] != lines[line_idx+i][idx-i]:
            return False
    return True

'''
S...
.A..
..M.
...X
'''
def check_left_diagonal_above(lines, line_idx, idx):
    for i in range(4):
        if XMAS[i] != lines[line_idx-i][idx-i]:
            return False
    return True

'''
...S
..A.
.M..
X...
'''
def check_right_diagonal_above(lines, line_idx, idx):
    for i in range(4):
        if XMAS[i] != lines[line_idx-i][idx+i]:
            return False
    return True

def part1(puzzle) -> int:
    xmas_count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 'X':
                continue

            if j >= 3:
                if check_before_in_row(puzzle[i], j):
                    xmas_count += 1

            if j <= len(puzzle[i]) - 4:
                if check_next_in_row(puzzle[i], j):
                    xmas_count += 1


            if i <= len(puzzle) - 4:
                if check_below(puzzle, i, j):
                    xmas_count += 1

            if i >= 3:
                if check_above(puzzle, i, j):
                    xmas_count += 1

            if j <= len(puzzle[i]) - 4 and i <= len(puzzle) - 4:
                if check_right_diagonal_below(puzzle, i, j):
                    xmas_count += 1

            if j >= 3 and i <= len(puzzle) - 4:
                if check_left_diagonal_below(puzzle, i, j):
                    xmas_count += 1

            if i >= 3 and j >= 3:
                if check_left_diagonal_above(puzzle, i, j):
                    xmas_count += 1

            if i >= 3 and j <= len(puzzle[i]) - 4:
                if check_right_diagonal_above(puzzle, i, j):
                    xmas_count += 1


    return xmas_count


def part2(puzzle):
    x_mas_count = 0
    MAS = 'MAS'
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] != 'A':
                continue

            if i >= 1 and i < len(puzzle) - 1 and j >= 1 and j < len(puzzle[i]) - 1:
                dig1 = puzzle[i-1][j-1] + puzzle[i][j] + puzzle[i+1][j+1]
                dig2 = puzzle[i-1][j+1] + puzzle[i][j] + puzzle[i+1][j-1]

                if (dig1 == MAS or dig1 == MAS[::-1]) and (dig2 == MAS or dig2 == MAS[::-1]):
                    x_mas_count += 1

    return x_mas_count


def main() -> None:
    with open('puzzle.txt', 'r') as f:
        puzzle = f.read().splitlines()
        print(part1(puzzle))
        print(part2(puzzle))



if __name__ == '__main__':
    main()
