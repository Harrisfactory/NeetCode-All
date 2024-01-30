class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        #declare counter and tracker
        perim_count = 0
        visited = []

        #cycle through matrix until we hit land
        for row in range(len(grid)):
            for col in range(len(grid[row])):
              perim_count +=  self.dfs(grid, row, col, visited)
              if grid[row][col] == 1:
                  break
            if grid[row][col] == 1:
                break
        
        return perim_count
        
    def dfs(self, grid, row, col, visited):
        #check bounds
        if row < 0 or row > len(grid) - 1 or col < 0 or col > len(grid[row]) - 1 or grid[row][col] == 0 or (row,col) in visited:
            return 0
        
        #on land, check perims
        visited.append((row,col))

        #compute counting logic
        cur_count = 0
        if row - 1 < 0 or grid[row - 1][col] == 0:
            cur_count+=1
        if row + 1 > len(grid) - 1 or grid[row + 1][col] == 0:
            cur_count+=1
        if col - 1 < 0 or grid[row][col - 1] == 0:
            cur_count+=1
        if col + 1 > len(grid[row]) - 1 or grid[row][col + 1] == 0:
            cur_count+=1

        #traverse cardinal, increment the result of each path
        cur_count+=self.dfs(grid, row - 1, col, visited)
        cur_count+=self.dfs(grid, row + 1, col, visited)
        cur_count+=self.dfs(grid, row, col - 1, visited)
        cur_count+=self.dfs(grid, row, col + 1, visited)
        
        #return the computed logic on this current path
        return cur_count
