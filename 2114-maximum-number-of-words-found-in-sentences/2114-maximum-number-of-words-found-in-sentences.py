class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        _max = float('-inf')
        for sentence in sentences:
            _max = max(_max, len(sentence.split(' ')))
        return _max
            
        