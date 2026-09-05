class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        using bruteforce, we can do dobule for-loop.
        fisrt loop indicate index1, second loop indicate index2.
        and then we can find the target. because the target is exactly one valid solution.
        We can use additional space O(1).
        left_num = numbers - target = [-2, -1, 0, 1]
        sorted_array can do binary search
        In the first loop, we can find the point which is 0. If there is no 0, we can use biggest number.
        THen we can do two pointer. Left pointer start from idx 0, right pointer start from idx when target - number is 0 or biggest number. 
        '''
        left, right = 0, len(numbers) - 1
        # If there is no target - numbers[idx] == 0 => Everything is less tan target
        if right == -1:
            right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] >= target:
                right -= 1
            else:
                left += 1

    