class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        dic1 = [0] * 26
        dic2 = [0] * 26
        for i in range(len(s1)):
            dic1[ord(s1[i])-ord('a')] += 1
            dic2[ord(s2[i])-ord('a')] += 1
        if dic1 == dic2:
            return True
        for i in range(1, len(s2)-len(s1)+1):
            dic2[ord(s2[i-1])-ord('a')] -= 1
            dic2[ord(s2[i+len(s1)-1])-ord('a')] += 1
            if dic1 == dic2:
                return True
        return False