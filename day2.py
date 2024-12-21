from typing import List
from day2_input_parser import parse_input

def main():
    lists = parse_input("day2_input.txt")
    print(get_safe_lists(lists))

# Part 1
def check_report_safe(list: List[int]) -> bool:
    is_increasing = all(list[i] < list[i + 1] for i in range(len(list) - 1))
    is_decreasing = all(list[i] > list[i + 1] for i in range(len(list) - 1))
    
    if not (is_increasing or is_decreasing):
        return False
    
    for i in range(len(list) - 1):
        x, y = list[i], list[i + 1]
        distance = abs(x - y)
        if distance < 1 or distance > 3:
            return False
    
    return True

# Part 2
def is_safe(list: List[int]) -> bool:
    if check_report_safe(list):
        return True
    
    for i in range(len(list)):
        modified_list = list[:i] + list[i+1:]
        if check_report_safe(modified_list):
            return True
    
    return False

def get_safe_lists(lists: List[List[int]]) -> int:
    count = 0
    for list in lists:
        if is_safe(list):
            count += 1
            
    return count

if __name__ == "__main__":
    main()
