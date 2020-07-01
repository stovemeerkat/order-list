from typing import List, Optional

def partition(arr: List[int], left: int, right: int) -> int:
    """Partition part of a list based on a pivot element
    The pivot element is always the element at index 'right'.
    When this function returns, 'arr' will be reorganized as follows:
    - outside of indices 'left' to 'right', it stays unchanged
    - between indices 'left' and 'right values smaller than the pivot are followed by the pivot
      element and then by values greater than or equal to the pivot

    Arguments:
    arr   - the list to operate on
    left  - start index of the list part that should be partitioned
    right - end index of the list part that should be partitioned

    Return value: new index of the pivot element
    """
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

def quickselect(arr: List[int], k: int) -> Optional[int]:
    """Return the k-smallest element of a list, i.e. the element which would be at index k if
       the list-was sorted
    """
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