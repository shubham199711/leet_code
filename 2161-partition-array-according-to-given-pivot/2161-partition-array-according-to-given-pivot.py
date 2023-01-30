class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return sorted(nums, key=lambda x: x-pivot and (1, -1)[x<pivot])
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
        
        