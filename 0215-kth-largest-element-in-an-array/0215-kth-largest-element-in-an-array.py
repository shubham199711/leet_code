from queue import PriorityQueue
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = PriorityQueue()
        for item in nums:
            q.put(-1 * item)
        prev = None
        for i in range(k):
            prev = q.get()
        return -1 * prev
            