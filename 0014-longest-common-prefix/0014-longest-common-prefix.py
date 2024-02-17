class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for char in strs[0]:
            new_str = ans + char
            for item in strs:
                if not item.startswith(new_str):
                    return ans
            ans = new_str
        return ans
                