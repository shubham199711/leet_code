def runLengthEncoding(_str):
    if _str == "":
        return ""
    count, _ans = 1, ""
    for index in range(1, len(_str)):
        if _str[index] != _str[index - 1]:
            _ans += f'{count}{_str[index - 1]}'
            count = 1
        else:
            count += 1
    _ans += f'{count}{_str[-1]}'
    return _ans

print(runLengthEncoding('aaaabcdaa'))
print(runLengthEncoding('aa'))
print(runLengthEncoding('abs'))
print(runLengthEncoding(''))
print(runLengthEncoding('aaaaaaaaaaaaaaaaaaaaa'))
print(runLengthEncoding('bababababbaba'))
