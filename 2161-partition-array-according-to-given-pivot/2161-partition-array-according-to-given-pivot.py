class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # [1, -1][x < pivot] is a trick to keep the order of array
        return sorted(nums, key=lambda x: x-pivot and [1, -1][x < pivot])
        # manual solution
        lessThenPivot = []
        moreThenPivot = []
        equalThenPivot = []
        for item in nums:
            if item == pivot:
                equalThenPivot.append(item)
            if item < pivot:
                lessThenPivot.append(item)
            if item > pivot:
                moreThenPivot.append(item)
        return lessThenPivot + equalThenPivot + moreThenPivot
        
        