class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        arr = [None for i in range(10)]
        def memo_square(x):
            index = ord(str(x)) - ord('0')
            if arr[index] is not None:
                return arr[index]
            arr[index] = x * x
            return arr[index]
        while n not in seen:
            seen.add(n)
            n = sum([memo_square(int(x)) for x in str(n)])
            if n == 1:
                return True
        return False
            
