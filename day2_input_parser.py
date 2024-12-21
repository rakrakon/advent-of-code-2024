from typing import List, Tuple

def parse_input(file_name: str) -> List[List[int]]:
    result = []

    with open(file_name, 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            result.append(numbers)
            
    return result