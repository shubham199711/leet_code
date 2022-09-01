def findFirstOne(arr):
    low, high = 0, len(arr) -1
    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == 1 and (mid == 0 or arr[mid -1] == 0):
            return mid
        if arr[mid] == 1:
            high = mid -1
        else:
            low = mid + 1
    return -1



assert(findFirstOne([0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ]) == 6)
assert(findFirstOne([]) == -1)
assert(findFirstOne([0,0,0,0,0,0,0]) == -1)
assert(findFirstOne([1,1,1,1,1,1,1]) == 0)