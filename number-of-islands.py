class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        island_counter: int = 0
        visited_islands: list = []

        #print map
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                island_found: bool = False
                if grid[row][col] not in visited_islands and grid[row][col] != "0":
                    island_found = self.dfs(grid, row, col)
                if island_found:
                    island_counter+=1
        return island_counter

    def dfs(self, grid, row, col):
        #base case
            #if the rows or columns are out of bounds during search
            #if were in water
            #if we have already visited this island
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row])-1 or grid[row][col] == "0":
            return False

        #on an univited island piece
        #visited_islands.append((row,col))
        #sink island
        grid[row][col] = "0"
        is_island: bool = True

        #traverse island with handshake
        if self.dfs(grid, row + 1, col):
            is_island = True
        if self.dfs(grid, row - 1, col):
            is_island = True
        if self.dfs(grid, row, col + 1):
            is_island = True
        if self.dfs(grid, row, col - 1):
            is_island = True

        #do we need to remove/pop? dont think so
        return is_island

#time complexity O(n * m) each node gets visited once
