class Solution:
    def climbStairs(self, n: int) -> int:
        # f(n) = f(n - 1) + f(n - 2)
        count = [i for i in range(46)]
        count[1] = 1
        count[2] = 2
        for i in range(3, 46):
            count[i] = count[i - 1] + count[i - 2]
        return count[n]