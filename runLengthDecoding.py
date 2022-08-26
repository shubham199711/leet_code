def runLengthDecoding(encodedStr):
    if encodedStr == '':
        return ''
    digit = ''
    _ans = ''
    for char in encodedStr:
        if char.isdigit():
            digit += char
        else:
            if digit == '':
                raise Exception('Bad Encoded String')
            _ans += int(digit) * char
            digit = ''
    return _ans


print(runLengthDecoding('4a1b1c1d2a'))
print(runLengthDecoding('2a'))
print(runLengthDecoding(''))
print(runLengthDecoding('21a'))
print(runLengthDecoding('1b1a1b1a1b1a1b1a2b1a1b1a'))
# print(runLengthDecoding('aa')) # exception test

