class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = [0] * 100001
        
        for num in nums:
            cnt[num] += 1
            if cnt[num] >= 2:
                return True
        return False