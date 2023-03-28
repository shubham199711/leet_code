class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        ord_a = ord('a')
        scoreWithWords = [(x, sum([score[ord(l) - ord_a] for l in x]))  for x in words ]
        cache = {}
        for item in letters:
            if cache.get(item) is not None:
                cache[item] += 1
            else:
                cache[item] = 1
        def dfs(i, _cache):
            if i >= len(scoreWithWords):
                return 0
            for item in scoreWithWords[i][0]:
                if _cache.get(item) is not None and _cache[item] > 0:
                    _cache[item] -= 1
                else:
                    return 0
            running_max = 0
            for j in range(i + 1, len(words)):
                running_max = max(running_max, dfs(j, _cache.copy()))
            return running_max + scoreWithWords[i][1]
         
        def main_dfs():
            return max([dfs(i, cache.copy()) for i in range(len(words))])
        
        return main_dfs()