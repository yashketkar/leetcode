class Solution:
    def revealSquare(self, board, click):
        x = click[0]
        y = click[1]
        if board[x][y] == 'M':
            board[x][y] == 'X'
        elif board[x][y] == 'E':
            adjacent = []
            if x-1>=0:
                adjacent.append([x-1, y])
                if y-1>=0:
                    adjacent.append([x-1, y-1])
                if y+1<len(board[x-1]):
                    adjacent.append([x-1, y+1])
            if y-1>=0:
                adjacent.append([x, y-1])
            if y+1<len(board[x]):
                adjacent.append([x, y+1])
            if x+1<len(board):
                adjacent.append([x+1, y])
                if y-1>=0:
                    adjacent.append([x+1, y-1])
                if y+1<len(board[x+1]):
                    adjacent.append([x+1, y+1])
            mine_count = 0
            for pos in adjacent:
                if board[pos[0]][pos[1]] == 'M':
                    mine_count += 1
            if mine_count == 0:
                board[x][y] = 'B'
                for i in adjacent:
                    self.revealSquare(board, i)
            else:
                board[x][y] = str(mine_count)


    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board:
            return board
        elif board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board
        else:
            self.revealSquare(board, click)
        return board
