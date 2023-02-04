class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # count of item + time to travel there
        lastG = True
        lastP = True
        lastM = True
        _ans = 0
        _sumArray = []
        _runningSum = 0
        
        for item in travel:
            _runningSum += item
            _sumArray.append(_runningSum)
            
            
        for i in range(len(garbage) - 1, 0, -1):
            item = garbage[i]
            
            if lastG == False and lastP == False and lastM == False:
                break
                
            if lastG and 'G' in item:
                lastG = False
                _ans += _sumArray[i - 1]
                
            if lastP and 'P' in item:
                lastP = False
                _ans += _sumArray[i - 1]
                
            if lastM and 'M' in item:
                lastM = False
                _ans += _sumArray[i - 1]
                
        return _ans + len(''.join(garbage))
            