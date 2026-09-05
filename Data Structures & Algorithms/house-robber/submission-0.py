class Solution:
    def rob(self, nums: List[int]) -> int:
        # 두 개의 인접한 집을 털지 못할 때, 최대로 털 수 있는 돈은?
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        dp = [0] * 101
        n = len(nums)

        if n < 1:
            return 0
        dp[0] = nums[0]

        if n < 2:
            return nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[n - 1]


        