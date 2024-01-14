class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #plan:
            #find and log all islands
            #return max(len(logged_islands)
        logged_islands: list = []

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                cur_island_ctr: int = 0
                cur_island_ctr = self.dfs(grid, row, col, cur_island_ctr)
                logged_islands.append(cur_island_ctr)
        return max(logged_islands)

    def dfs(self, grid, row, col, cur_island_ctr):
        #bounds
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row]) -1 or grid[row][col] == 0:
            return 0

        #sink piece of island
        cur_island_ctr=1
        grid[row][col] = 0

        #traverse around the island
        cur_island_ctr += self.dfs(grid, row + 1, col, cur_island_ctr)
        cur_island_ctr += self.dfs(grid, row - 1, col, cur_island_ctr)
        cur_island_ctr += self.dfs(grid, row, col + 1, cur_island_ctr)
        cur_island_ctr += self.dfs(grid, row, col - 1, cur_island_ctr)

        return cur_island_ctr
