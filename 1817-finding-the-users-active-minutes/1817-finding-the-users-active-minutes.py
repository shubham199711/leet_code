class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mapping = {}
        ans = [0] * k
        for _id, time in logs:
            if mapping.get(_id) is not None:
                mapping[_id].add(time)
            else:
                 mapping[_id] = set([time])
        for key,value in mapping.items():
            ans[len(value) -1] = ans[len(value) -1] + 1
        return ans