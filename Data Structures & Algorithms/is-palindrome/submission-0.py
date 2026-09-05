class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alnum_checked_s = []
        for c in s:
            if c.isalnum():
                alnum_checked_s.append(c)
        start, end = 0, len(alnum_checked_s) - 1
        while start < end:
            print(alnum_checked_s[start], alnum_checked_s[end])
            if alnum_checked_s[start] != alnum_checked_s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True