class Solution(object):
    def pay_a_visit(self, i, j, grid):
        grid[i][j] = '0'
        if i<self.row_len-1 and grid[i+1][j] == '1':
            self.pay_a_visit(i+1, j, grid)
        if j<self.col_len-1 and grid[i][j+1] == '1':
            self.pay_a_visit(i, j+1, grid)
        if i>0 and grid[i-1][j] == '1':
            self.pay_a_visit(i-1, j, grid)
        if j>0 and grid[i][j-1] == '1':
            self.pay_a_visit(i, j-1, grid)
        pass

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.row_len = len(grid)
        self.col_len = len(grid[0])
        count = 0
        for i in range(self.row_len):
            for j in range(self.col_len):
                if grid[i][j]== '1':
                    self.pay_a_visit(i, j, grid)
                    count += 1
        return count
