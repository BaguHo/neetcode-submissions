class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        for i in range(len(heights)):
            for j in range(len(heights)):
                res = max(res, (i - j) * min(heights[i], heights[j]))
        return res