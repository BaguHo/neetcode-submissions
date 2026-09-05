class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen_s = dict()
        seen_t = dict()
        for c in s:
            if c not in seen_s:
                seen_s[c] = 1
            else:
                seen_s[c] += 1
        for c in t:
            if c not in seen_t:
                seen_t[c] = 1
            else:
                seen_t[c] += 1
        
        return True if seen_s == seen_t else False