def printRoman(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    _ans = ''
    while number:
        div = number // num[i]
        number %= num[i]
        print(f'{div = }, {number = }, { i  = }')
        _ans += (sym[i] * div)
        i -= 1
    return _ans
  
if __name__ == "__main__":
    number = 3549
    print(printRoman(number))