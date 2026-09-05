class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        n = len(s)
        # 회문이 홀수인 경우
        for i in range(n):
            curStr = s[i]
            f,b = i, i
            while True:
                f -= 1
                b += 1
                if 0 <= f < n and 0 <= b < n:
                    if s[f] == s[b]:
                        curStr = s[f] + curStr + s[b]
                        if len(res) < len(curStr):
                            res = curStr
                    else:
                        break
                else:
                    break
    
        # 회문이 짝수인 경우
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                curStr = s[i] + s[i + 1]
            else:
                continue
            if len(res) < len(curStr):
                res = curStr
            f, b = i, i + 1
            while True:
                f -= 1
                b += 1
                if 0 <= f < n and 0 <= b < n:
                    if s[f] == s[b]:
                        curStr = s[f] + curStr + s[b]
                        if len(res) < len(curStr):
                            res = curStr
                    else:
                        break
                else:
                    break
        
        return res