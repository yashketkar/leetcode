class Solution:
    def contains_duplicates(self, pa):
        no_zero = [y for y in pa if y != '.']
        if len(set(no_zero)) != len(no_zero):
            return True
        return False

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        pa = board
        for row in pa:
            if self.contains_duplicates(row):
                return False
        for i in range(len(pa[0])):
            col = [x[i] for x in pa]
            if self.contains_duplicates(col):
                return False
        for i in [0,3,6]:
            for j in [0,3,6]:
                sub = [pa[i+0][j+0], pa[i+0][j+1], pa[i+0][j+2], pa[i+1][j+0], pa[i+1][j+1], pa[i+1][j+2], pa[i+2][j+0], pa[i+2][j+1], pa[i+2][j+2]]
                if self.contains_duplicates(sub):
                    return False    
        return True
