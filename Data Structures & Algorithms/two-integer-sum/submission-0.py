class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            cur = target - num
            if cur in hash_map:
                return [hash_map[cur], i]
            hash_map[num] = i