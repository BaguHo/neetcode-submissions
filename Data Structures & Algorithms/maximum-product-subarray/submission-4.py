class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = max(nums)

        # 0을 기준으로 subarray 만들기
        cur_arr = []
        sub_arr = []
        for num in nums:
            if num == 0:
                if cur_arr:
                    sub_arr.append(cur_arr)
                    cur_arr = []
            else:
                cur_arr.append(num)
        if cur_arr:
            sub_arr.append(cur_arr)

        for arr in sub_arr:
            minus_idxs = [i for i,num in enumerate(arr) if num < 0]

            if len(minus_idxs) % 2 == 0:
                res = max(res, math.prod(arr))
            else:
                idxs = [minus_idxs[0], minus_idxs[-1]]
                for cur_idx in idxs:
                    left_part = arr[:cur_idx]
                    right_part = arr[cur_idx + 1:]
                    
                    if left_part:
                        res = max(res, math.prod(left_part))
                    if right_part:
                        res = max(res, math.prod(right_part))
        return res