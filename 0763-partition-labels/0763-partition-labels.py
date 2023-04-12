class Solution():
    def partitionLabels(self, S):
        dic = {}
        for i, char in enumerate(S):
            dic[char] = i
        res = []
        currLen = 0
        hi = 0
        for i, char in enumerate(S):
            hi = max(hi, dic[char])
            if i == hi:
                res.append(i - currLen + 1)
                currLen = i+1
        return res