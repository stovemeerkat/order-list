from typing import List, Optional

# Focuses on the contents of list 'arr' between indices 'left' and 'right' (inclusive) and partitions them based on a pivot value
# The pivot value is always the value at index 'right'.
# Outside of the indices 'left' and 'right', 'arr' will stay unchanged.
# Between these indices the array will be reorganized as follows:
# Values less than the pivot value will come first, followed by the pivot value and then the values greater then the pivot
# The return value is the new index of the pivot value
def partition(arr: List[int], left: int, right: int) -> int:
    assert 0 <= left and left < len(arr) and 0 <= right and right < len(arr)
    pivot: int = arr[right]
    i, j = left, right - 1
    while True:
        while i < right and arr[i] < pivot:
            i += 1
        while j >= left and arr[j] >= pivot:
            j -= 1
        if i >= j:
            break
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[right] = arr[right], arr[i]
    return i

# Returns the 'k'-th smalles element of list 'arr'.
# More specifically, that is the element that would be at index 'k' if the list was sorted
def quickselect(arr: List[int], k: int) -> Optional[int]:
    if k < 0 or k >= len(arr):
        return None
    tmp_arr: List[int] = arr[:]
    def qs(left: int, right: int) -> int:
        if left == right:
            return left
        partition_index = partition(tmp_arr, left, right)
        if partition_index == k:
            return partition_index
        if partition_index > k:
            return qs(left, partition_index - 1)
        else:
            return qs(partition_index + 1, right)
    result_index = qs(0, len(arr) - 1)
    return tmp_arr[result_index]