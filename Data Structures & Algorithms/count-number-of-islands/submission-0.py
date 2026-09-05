class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(cur):
            if cur[0] < 0 or cur[1] < 0 or cur[0] >= len(grid) or cur[1] >= len(grid[0]) or grid[cur[0]][cur[1]] == "0":
                return
            grid[cur[0]][cur[1]] = "0"

            dfs([cur[0] + 1, cur[1]])
            dfs([cur[0] - 1, cur[1]])
            dfs([cur[0], cur[1] + 1])
            dfs([cur[0], cur[1] - 1])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs([i,j])
                    res += 1

        return res