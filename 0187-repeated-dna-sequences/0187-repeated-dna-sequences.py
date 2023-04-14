class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seqCount = {}
        for i in range(0, len(s) - 9):
            _seq = s[i: i + 10]
            seqCount[ _seq ] = seqCount.get(_seq, 0) + 1
        ans = []
        for key, value in seqCount.items():
            if value > 1:
                ans.append(key)
        return ans
            
        