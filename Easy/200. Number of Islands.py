land = [["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]]

visited = []
def dfs(grid, i, j):
    if (grid[i][j] == 0):
        return False
    dfs(grid,i,j+1)
    dfs(grid,i,j+1)
    dfs(grid,i,j+1)
    dfs(grid,i,j+1)

    pass


def number_of_island(land):
    pass


number_of_island(land)
