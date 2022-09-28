
def helper(arr, _ans, currentAns, currentWord, j):
    if currentWord == '':
        return _ans.append(currentAns)
    for i, innerItem in enumerate(arr):
        if i == j:
            continue
        if currentWord.startswith(innerItem):
            currentAns.append(innerItem)
            helper(arr, _ans, currentAns, currentWord[len(innerItem):] , j)
    return _ans

def breakWord(arr):
    _ans = []
    _ = [helper(arr, _ans, [], x, i) for i, x in enumerate(arr)]
    return _ans


_list = ['rockstar', 'rock', 'star', 'baseball', 'base', 'ball']
print(breakWord(_list))