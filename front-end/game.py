import tkinter
from config import *

class gomoku:
    def __init__(self, master):
        self.master = tkinter.Toplevel(master)

        self.gameFrame = tkinter.Frame(self.master)
        self.canvas = tkinter.Canvas(self.gameFrame)

        self.infoFrame = tkinter.Frame(self.master)
        # button
        self.exitBtn = tkinter.Button(self.infoFrame)
        # label
        self.player_1_Label = tkinter.Label(self.infoFrame)
        self.player_2_Label = tkinter.Label(self.infoFrame)
        self.winner_Label = tkinter.Label(self.infoFrame)
        # image label
        self.player_1_icon = tkinter.Label(self.infoFrame)
        self.player_2_icon = tkinter.Label(self.infoFrame)

        self.setConfig()
        # self.master.mainloop()

    def setConfig(self):
        self.master.geometry("900x650")
        self.master.config(bg=bg_color)
        self.master.withdraw()
        #==========================================================================================

        # self.gameFrame.config()
        self.gameFrame.grid(row=0,column=0,padx=10,pady=10)

        # canvas
        self.canvas.config(width=620,height=620,highlightthickness=1, highlightbackground="pink")
        self.canvas.pack()
        self.drawGrid()
        
        #==========================================================================================
        self.infoFrame.config(bg=bg_color)
        self.infoFrame.grid(row=0,column=1,sticky='n')

        # player 1 label
        self.player_1_Label.config(text='Player 1',bg=bg_color,fg=player_1_color,font=("Calibri",20))
        self.player_1_Label.grid(row=0,column=0)
        # player 2 label
        self.player_2_Label.config(text="Player 2",bg=bg_color,fg=player_2_color,font=("Calibri",20))
        self.player_2_Label.grid(row=1,column=0)
        # player 1 icon
        self.player_1_icon.config(image=tkinter.PhotoImage(file='images/player_1.gif'))
        self.player_1_icon.grid(row=0,column=1)

        # winner label
        self.winner_Label.config(bg=bg_color,fg='yellow',font=("Calibri",20))
        self.winner_Label.grid(row=3,column=0,pady=20)

        # exit button
        self.exitBtn.config(text="Exit",font=("Calibri",13))
        self.exitBtn.grid(row=2,column=0,ipadx=30,pady=20)

    def start(self):
        self.master.deiconify()
        self.master.update()

    def stop(self):
        self.master.withdraw()

    def restart(self):
        self.canvas.delete(tkinter.ALL)
        self.drawGrid()

    def drawGrid(self):
        for i in range(0,21):
            x = y = 30 * i + 10
            # horizontal
            self.canvas.create_line(10,y,610,y)
            # vertical
            self.canvas.create_line(x,10,x,610)

    def draw(self,chess,cor):
        row, col = cor
        x, y = self.toCor(row,col)
        # check if position is out of range
        if x <= 0 or x >= 610 or y <= 0 or y >= 610:
            return False

        if chess == 2:
            # draw O
            self.canvas.create_oval(x+5,y+5,x+25,y+25,outline=player_2_color,width=3)
        elif chess == 1:
            # draw X
            self.canvas.create_line(x+5,y+5,x+25,y+25,fill=player_1_color,width=3)
            self.canvas.create_line(x+25,y+5,x+5,y+25,fill=player_1_color,width=3)
        return True

    def toRow(self,x,y):
        row = int(y / 30)
        col = int(x / 30)
        return [row,col]

    def toCor(self,row,col):
        x = col * 30 + 10
        y = row * 30 + 10
        return [x,y]

# if __name__ == "__main__":
#     master = tkinter.Tk('Demo')
#     master.withdraw()
#     game = gomoku(master)
#     game.start()