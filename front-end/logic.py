#  0: can move
#  1: win
# -1: can not move

class logic:
    def __init__(self,maze):
        self.maze = maze
        self.rows = len(self.maze)
        self.cols = len(self.maze)

    def reset(self,row,col):
        for i in range(self.rows):
            for j in range(self.cols):
                self.maze[i][j] = 0

    def check(self,row,col,player):
        if self.canMove(row,col):
            self.maze[row][col] = player
            # if self.isWin(row,col):
            #     return 1
            # return 0
            return self.isWin(row,col)
        else:
            return -1

    def canMove(self,row,col):
        if row < 0 or row >= self.rows or col < 0 or col > self.cols:
            return False
        elif self.maze[row][col] != 0:
            return False
        else:
            return True

    def isWin(self,row,col):
        # horizontal
        for i in range(-4,1):
            if (row+i < 0) or (row+i+4 > self.rows):
                continue
            cnt = 0
            for j in range(5):
                if self.maze[row+i+j][col] == self.maze[row][col]:
                    cnt += 1
                else:
                    break
            if cnt == 5:
                return True

		# vertical checking
        for i in range(-4,1):
            if (col+i < 0) or (col+i+4 > self.cols):
                continue
            cnt = 0
            for j in range(5):
                if self.maze[row][col+i+j] == self.maze[row][col]:
                    cnt += 1
                else:
                    break
            if cnt == 5:
                return True

		#diagonal checking from left to right
            for i in range(-4,1):
                if (row+i < 0) or (row+i+4 > self.rows) or (col+i < 0) or (col+i+4 > self.cols):
                    continue
                cnt = 0
                for j in range(5):
                    if self.maze[row+i+j][col+i+j] == self.maze[row][col]:
                        cnt += 1
                    else:
                        break
                if cnt == 5:
                    return True

		#diagonal checking from right to left
            for i in range(-4,1):
                if (row+i < 0) or (row+i+4 > self.rows) or (col-i-4 < 0) or (col-i > self.cols):
                    continue
                cnt = 0
                for j in range(5):
                    if self.maze[row+i+j][col-i-j] == self.maze[row][col]:
                        cnt += 1
                    else:
                        break
                if cnt == 5:
                    return True

            return False

# maze = [
#         [1,0,0,0,0],
#         [0,1,0,0,0],
#         [0,0,1,0,0],
#         [0,0,0,1,0],
#         [0,0,0,0,0],
# ]
# row = 4
# col = 4
# player = 1
# game = logic(maze)
# rst = game.check(row,col,player)
# print(rst)