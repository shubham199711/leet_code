def listOfAnagram(arr):
    m = {}
    for item in arr:
        sortedItem = ''.join(sorted(item))
        if m.get(sortedItem) is not None:
            temp = m[sortedItem]
            temp.append(item)
            m[sortedItem] = temp
        else:
            m[sortedItem] = [item]
    _ans = []
    for key in m:
        _ans.append(m[key])
    return _ans

if __name__ == "__main__":
    _list = ["eat", "tea", "tan", "ate", "nat", "bat" ]
    print(listOfAnagram(_list))
