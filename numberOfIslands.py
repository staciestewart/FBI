# Given a 2d grid map of '1's (land) and '0's (water), 
# count the number of islands. An island is surrounded 
# by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four 
# edges of the grid are all surrounded by water.


def numIslands(self, grid):
    def sink(i, j):
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
            grid[i][j] = '0'
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
            return 1
        return 0
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))
