class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # i가 맨 왼쪽 left로 사용됨
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum == 0:
                    res.append([nums[i],nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                            l += 1 
                elif threeSum > 0:
                    r -= 1
                else:
                    l += 1
        return res