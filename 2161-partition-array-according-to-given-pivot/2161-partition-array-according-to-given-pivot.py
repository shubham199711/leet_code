class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
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
        
        