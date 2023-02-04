class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answers = []
        for i, item in enumerate(boxes):
            _ans = 0
            for j in range(i):
                if boxes[j] == '1':
                    _ans += abs(j -i)
            for k in range(i + 1, len(boxes)):
                if boxes[k] == '1':
                    _ans += abs(k -i)
            answers.append(_ans)
        return answers
                
                
        