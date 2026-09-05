class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        # 홀수인 경우
        for i in range(n):
            l, r = i, i
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        # 짝수인 경우
        for i in range(n - 1):
            l, r = i, i + 1
            while 0 <= l < n and 0 <= r < n and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        return res