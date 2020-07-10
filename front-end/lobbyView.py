import tkinter

class lobbyView:
    def __init__(self):
        self.master = tkinter.Tk(className=" HLC Gomoku")

        self.roomFrame = tkinter.LabelFrame(self.master)
        self.roomList = tkinter.Listbox(self.roomFrame)

        self.funcFrame = tkinter.Frame(self.master)
        self.codeEntry = tkinter.Entry(self.funcFrame)
        self.createBtn = tkinter.Button(self.funcFrame)
        self.joinBtn = tkinter.Button(self.funcFrame)

        self.setView()

    def setView(self):
        # screen
        self.master.geometry("400x600")
        self.master.config(bg="#333")
        # self.master.minsize(400,600)
        # self.master.maxsize(400,600)

        #==========================================================================================
        # room frame
        self.roomFrame.config(text="Room",bg="#333",fg="#fff",bd=0,font=("Calibri",20))
        self.roomFrame.pack()
        
        # room listbox
        self.roomList.config(width=40,height=15,bd=0,bg="#333",fg="#fff",font=("Calibri",13),
                            selectmode="single",selectbackground="#33FF71")
        self.roomList.pack()

        #==========================================================================================
        # function frame
        self.funcFrame.config(bg="#333")
        self.funcFrame.pack()

        # room code entry
        self.codeEntry.config(width=30,font=("Calibri",13))
        self.codeEntry.grid(row=0,column=0,pady=10)

        # join button
        self.joinBtn.config(text="JOIN",font=("Calibri",13),width=30,command=self.joinFunc)
        self.joinBtn.grid(row=1,column=0,pady=10)

        # create button
        self.createBtn.config(text="CREATE",font=("Calibri",13),width=30,command=self.createFunc)
        self.createBtn.grid(row=2,column=0,pady=10)

    def start(self):
        while True:
            data = input(">>> ")
            self.addRommList(data)
            self.master.update()

    def addRommList(self,data):
        self.roomList.insert('end',data)

    def joinFunc(self):
        print("join")

    def createFunc(self):
        print("create")

if __name__ == "__main__":
    lobby = lobbyView()
    lobby.start()
