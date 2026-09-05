class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        barket_pair = {'}': '{', ')': '(', ']': '['}
        for c in s:
            if c in barket_pair:
                if not stack or stack[-1] != barket_pair[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack