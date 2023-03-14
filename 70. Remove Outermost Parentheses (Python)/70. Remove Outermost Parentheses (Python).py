class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        open = 0
        for c in s:
            if c == '(' and open > 0: ans.append(c)
            if c == ')' and open > 1: ans.append(c)
            open += 1 if c == '(' else -1
        return "".join(ans)
