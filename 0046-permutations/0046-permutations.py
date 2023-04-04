class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def per(_list, i, n):
            if i == n:
                ans.append(_list.copy())
            else:
                for j in range(i, n):
                    _list[i], _list[j] = _list[j], _list[i]
                    per(_list, i + 1, n)
                    _list[i], _list[j] = _list[j], _list[i]
        per(nums, 0, len(nums))
        return ans
        