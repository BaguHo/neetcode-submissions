class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1e9 for _ in range(len(nums) + 1)]

        for i in range(1, len(nums) + 1):
            dp[i] = max(nums[i - 1], dp[i - 1] + nums[i - 1])
        
        return max(dp)
        
