import tkinter

class gomokuView:
    def __init__(self):
        self.master = tkinter.Tk(className=" HLC Gomuku")
        
        self.gameFrame = tkinter.Frame(self.master)
        self.canvas = tkinter.Canvas(self.gameFrame)

        self.infoFrame = tkinter.Frame(self.master)
        self.readyBtn = tkinter.Button(self.infoFrame)
        self.exitBtn = tkinter.Button(self.infoFrame)
        self.player_1_Label = tkinter.Label(self.infoFrame)
        self.player_2_Label = tkinter.Label(self.infoFrame)

        self.setConfig()
        self.bindEvent()

    def setConfig(self):
        self.master.geometry("900x650")
        self.master.config(bg="#333")
        # self.master.maxsize(900,650)
        # self.master.minsize(900,650)
        #==========================================================================================

        # self.gameFrame.config()
        self.gameFrame.grid(row=0,column=0,padx=10,pady=10)

        # canvas
        self.canvas.config(width=620,height=620,highlightthickness=1, highlightbackground="pink")
        self.canvas.pack()
        self.drawGrid()
        
        #==========================================================================================
        self.infoFrame.config(bg="#333")
        self.infoFrame.grid(row=0,column=1)

        # player 1 label
        self.player_1_Label.config(text="Player 1",bg="#333",fg="#fff",font=("Calibri",20))
        self.player_1_Label.grid(row=0,column=0)

        # player 2 label
        self.player_2_Label.config(text="Player 2",bg="#333",fg="#fff",font=("Calibri",20))
        self.player_2_Label.grid(row=1,column=0)

        # ready button
        self.readyBtn.config(text="Ready",font=("Calibri",13))
        self.readyBtn.grid(row=2,column=0,ipadx=20,pady=20)

        # exit button
        self.exitBtn.config(text="Exit",font=("Calibri",13))
        self.exitBtn.grid(row=2,column=1,ipadx=30,pady=20)

    def start(self):
        self.master.mainloop()

    def drawGrid(self):
        for i in range(0,21):
            x = y = 30 * i + 10
            # horizontal
            self.canvas.create_line(10,y,610,y)
            # vertical
            self.canvas.create_line(x,10,x,610)

    def draw(self,chess,x,y):
        # check if position is out of range
        print(f"{x} {y}")
        if x <= 0 or x >= 610 or y <= 0 or y >= 610:
            return False

        if chess == 0:
            self.canvas.create_oval(x+5,y+5,x+25,y+25,outline="blue",width=3)
        elif chess == 1:
            self.canvas.create_line(x+5,y+5,x+25,y+25,fill="red",width=3)
            self.canvas.create_line(x+25,y+5,x+5,y+25,fill="red",width=3)
        return True

    def bindEvent(self):
        # Mouse Event
        self.master.bind('<Double-Button-1>',self.mousePosition)
    
    def mousePosition(self,event):
        chess = 1
        row, col = self.toRow(event.x-10,event.y-10)
        x, y = self.toCor(row,col)
        if self.draw(chess,x,y):
            print(f"[{chess}] {row} {col}")
            return row,col

    def toRow(self,x,y):
        row = int(y / 30)
        col = int(x / 30)
        return [row,col]

    def toCor(self,row,col):
        x = col * 30 + 10
        y = row * 30 + 10
        return [x,y]


if __name__ == "__main__":
    game = gomokuView()
    game.start()