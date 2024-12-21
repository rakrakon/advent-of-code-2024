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

def main() -> None:
    with open('puzzle.txt', 'r') as f:
        print(part1(f.read().splitlines()))



if __name__ == '__main__':
    main()
