class Solution(object):
    def letterCombinations_old(self, digits):
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

    def letterCombinationsWithRecursion(self, digits):
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
        ans  = []
        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                ans.append(currentStr)
                return
            for item in char_map[digits[i]]:
                backtrack(i + 1, currentStr + item)
        backtrack(0, "")
        return ans

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def letterCombinations(self, digits):
        if not len(digits):
            return []
        mapping = {
            '0': '',
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = [""]
        for d in digits:
            possible_char = mapping.get(d, "")
            temp = []
            for x in ans:
                for char in possible_char:
                    temp.append(x + char)
            ans = temp
        return ans
        
