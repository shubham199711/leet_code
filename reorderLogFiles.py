class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for item in logs:
            if item.split()[1].isdigit():
                digits.append(item)
            else:
                letters.append(item)
        letters.sort(key = lambda x: x.split()[0])
        letters.sort(key = lambda x: x.split()[1:])
        return letters + digits 
        