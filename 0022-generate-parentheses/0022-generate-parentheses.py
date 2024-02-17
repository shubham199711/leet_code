class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        # parentheses string, open count, close_count
        stack = [('(', 1, 0)]
        ans = []
        while stack:
            curr_ans, open_count, close_count = stack.pop()
            if len(curr_ans) == 2 * n:
                ans.append(curr_ans)
                continue
            if open_count < n:
                stack.append((curr_ans + '(', open_count + 1, close_count))
            if close_count < open_count:
                stack.append((curr_ans + ')', open_count, close_count + 1))
        return ans
