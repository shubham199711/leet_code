class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #return str(int(num1) * int(num2))
        n1, n2 = int(num1[0]), int(num2[0])
        ord_0 = ord("0")
        for item in num1[1:]:
            n1 *= 10
            n1 += ord(item)-ord_0
        for item in num2[1:]:
            n2 *= 10
            n2 += ord(item)-ord_0
        return str(n1 * n2)