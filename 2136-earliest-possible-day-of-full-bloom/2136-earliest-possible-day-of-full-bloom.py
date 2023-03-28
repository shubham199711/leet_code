class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        v = [(growTime[i], plantTime[i]) for i in range(len(plantTime))]
        v.sort(key= lambda x: x[0],reverse = True)
        day, lpd = 0, 0
        for p in v:
            lpd += p[1]
            day = max(day, lpd + p[0])
        return day