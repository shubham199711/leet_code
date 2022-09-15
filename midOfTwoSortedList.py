def midOfTwoList(list1,list2):
    mid = (len(list1) + len(list2)) // 2
    pointer1,pointer2 = 0, 0
    runningMidPointer,runningNum = 0, -1
    while pointer1 < len(list1) and pointer2 < len(list2) and runningMidPointer < mid:
        if list1[pointer1] <= list2[pointer2]:
            pointer1 += 1
            runningNum = list1[pointer1]
        else:
            pointer2 += 1
            runningNum = list2[pointer2]
        runningMidPointer += 1
    if mid == runningMidPointer:
        return runningNum
    while pointer1 < len(list1) and runningMidPointer < mid:
        pointer1 += 1
        runningNum = list1[pointer1]
        runningMidPointer += 1
    while pointer2 < len(list2) and runningMidPointer < mid:
        pointer2 += 1
        runningNum = list2[pointer2]
        runningMidPointer += 1
    return runningNum



if __name__ == "__main__":
    list1 = [1 ,10,15,16,18]
    list2 = [2 ,11,17,18,20, 42]
    print(sorted(list1 + list2))
    print(midOfTwoList(list1, list2))