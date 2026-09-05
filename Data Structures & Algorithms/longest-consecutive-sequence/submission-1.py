class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_num = 0
        
        for num in nums:
            if num - 1 not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                longest_num = max(length, longest_num)
        
        return longest_num