class Solution(object):
    def letterCombinations(self, digits):
        if not digits: 
            return []
        char_map = { 
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        chars = [char_map[d] for d in digits]
        l = list(itertools.product(*chars))
        return [''.join(i) for i in l]