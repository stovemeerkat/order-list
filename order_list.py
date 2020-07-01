from typing import List, Dict, Optional
from quickselect import quickselect

def distinct(input: List[int]) -> List[int]:
    result: List[int] = []
    for x in input:
        if not x in result:
            result.append(x)
    return result

def simple_order_dict(input: List[int]) -> Dict[int, int]:
    sorted_distinct: List[int] = sorted(distinct(input))
    return {sorted_distinct[i]: i for i in range(len(sorted_distinct))}

def quick_order_dict(input: List[int]) -> Dict[int, int]:
    result: Dict[int, int] = {}
    last_value = None
    next_number = 0
    for k in range(len(input)):
        kth_element: Optional[int] = quickselect(input, k)
        if kth_element is None:
            raise TypeError
        if kth_element == last_value:
            continue
        result[kth_element] = next_number
        last_value = kth_element
        next_number += 1
    return result
    
    
def to_order_list(input: List[int]) -> List[int]:
    order_dict: Dict[int, int] = quick_order_dict(input)
    return list(map(lambda x: order_dict[x], input))

# test case
if __name__ == '__main__':
    arr = [9, 8, 17, 18, 16, 4, 14, 9, 16, 17]
    print(to_order_list(arr))