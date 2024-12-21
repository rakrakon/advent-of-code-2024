from typing import List
from day1_input_parser import parse_input

frequency = {}

def main():
    # Part 1
    list1, list2 = parse_input("day1_input.txt")
    
    list1.sort()
    list2.sort()
    
    print(calc_total_distance(list1, list2))
    
    # Part 2
    left_list, right_list = parse_input("day1_input.txt")
    calc_frequency(right_list)
    
    print(calc_similarity_score(left_list))


# Part 1
def calc_total_distance(list1: List[int], list2: List[int]) -> int:
    list1.sort()
    list2.sort()
    
    sum = 0
    max_size = max(len(list1), len(list2))
    for i in range(0, max_size, 1):
        num1 = 0
        num2 = 0
        try:
            num1 = list1[i]
        except IndexError:
            num1 = 0
            
        try:
            num2 = list2[i]
        except:
            num2 = 0
            
        distance = abs(num1 - num2)
        sum += distance
            
    return sum

# Part 2
def calc_similarity_score(list: List[int]) -> int:
    sum = 0
    for v in list:
        sum += v * frequency.get(v, 0)
        
    return sum
        
def calc_frequency(list: List[int]) -> None:
    for v in list:
        num = frequency.get(v, 0)
        frequency[v] = num + 1

if __name__ == '__main__':
    main()