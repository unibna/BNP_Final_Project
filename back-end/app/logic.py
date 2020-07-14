#  0: can move
#  1: win
# -1: can not move

class logic:
    def __init__(self,maze):
        self.maze = maze
        self.rows = 20
        self.cols = 20

    def reset(self):
        for i in range(self.rows):
            for j in range(self.cols):
                self.maze[i][j] = 0

    def display_maze(self):
        for row in self.maze:
            print(row)

    def check(self,row,col,player):
        if self.canMove(row,col):
            self.maze[row][col] = player
            self.display_maze()
            if self.winCheck(row,col,player):
                return 1
            return 0
        else:
            return -1

    def canMove(self,row,col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False
        elif self.maze[row][col] != 0:
            return False
        else:
            return True
    	
    def winCheck(self,row,col,player):
        selectedCell = (row,col)
        size = 20
        count = player
        cur_row = selectedCell[0]
        cur_col = selectedCell[1] - 1
        # check row left
        while cur_col > -1 and self.maze[cur_row][cur_col] == player:
            count += player
            cur_col -= 1
        cur_col = selectedCell[1] + 1
        # check row right
        while cur_col < size and self.maze[cur_row][cur_col] == player:
            count += player
            cur_col += 1

        if count == player*5:
            return True
        # check column up
        count = player
        cur_col = selectedCell[1]
        cur_row = selectedCell[0] - 1
        while cur_row > -1 and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row -= 1
        # check column down
        cur_row = selectedCell[0] + 1
        while cur_row < size and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row += 1
        if count == player*5:
            return True
        # check diagonal 
        count = player
        cur_row = selectedCell[0] - 1
        cur_col = selectedCell[1] - 1
        while cur_row > -1 and cur_col > -1 and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row -= 1
            cur_col -= 1
        cur_row = selectedCell[0] + 1
        cur_col = selectedCell[1] + 1
        while cur_row < size and cur_col < size and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row += 1
            cur_col += 1
        if count == player*5:
            return True
        # check diagonal 
        count = player
        cur_row = selectedCell[0] - 1
        cur_col = selectedCell[1] + 1
        while cur_row > -1 and cur_col < size and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row -= 1
            cur_col += 1
        cur_row = selectedCell[0] + 1
        cur_col = selectedCell[1] - 1
        while cur_row < size and cur_col > -1 and self.maze[cur_row][cur_col] == player:
            count += player
            cur_row += 1
            cur_col -= 1
        if count == player*5:
            return True
        return False 



# maze = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     ]

# l = logic(maze)
# rst = l.winCheck(3,10,1)
# print(rst)