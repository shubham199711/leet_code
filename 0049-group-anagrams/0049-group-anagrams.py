class Solution:
    def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        ans = []
        arr = [(item, "".join(sorted(item))) for item in arr]
        cache = {}
        for item, sorted_item in arr:
            if cache.get(sorted_item) is None:
                cache[sorted_item] = []
            cache.get(sorted_item).append(item)
        for _, values in cache.items():
            ans.append(values)
        return ans