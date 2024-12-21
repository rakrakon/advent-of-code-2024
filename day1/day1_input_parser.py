from typing import List, Tuple

def parse_input(file_name: str) -> Tuple[List[int], List[int]]:
    left_list = []
    right_list = []
    
    with open(file_name, 'r') as file:
        for line in file:
            left_num, right_num = line.split()
            left_list.append(int(left_num))
            right_list.append(int(right_num))
            
    return left_list, right_list