class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        stack = [('(', 1, 0)]
        ans = []
        open_and_close_pan_count = 2 * n
        while stack:
            cur_ans, n_left, n_right = stack.pop()
            if len(cur_ans) == open_and_close_pan_count:
                ans.append(cur_ans)
                continue
            if n_left < n: # if less then n number of par
                stack.append((cur_ans + '(', n_left + 1, n_right))
            if n_right < n_left: # if less then open par
                stack.append((cur_ans + ')', n_left, n_right + 1))
        return ans
        