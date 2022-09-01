def binarySearch(arr, find):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == find:
            return mid
        if find < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

assert binarySearch([1, 3, 4, 5, 6], 3) == 1, "Error: in binary search"
assert binarySearch([], 3) == -1, "Error: in binary search"
assert binarySearch([1, 3, 4, 5, 6], 6) == 4, "Error: in binary search"