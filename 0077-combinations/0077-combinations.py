class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nlist = [x for x in range(1, n + 1)]
        prev = [[]]
        for item in nlist:
            prev += [x + [item] for x in prev if len(x) < k]
        return [x for x in prev if len(x) == k]
        