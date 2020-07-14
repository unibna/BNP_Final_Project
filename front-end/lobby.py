import tkinter

class lobbyView:
    def __init__(self,master):
        self.mainFrame = tkinter.Frame(master)

        # Room Frame
        self.roomFrame = tkinter.Frame(self.mainFrame)
        self.roomList = tkinter.Listbox(self.mainFrame)
        self.notiLabel = tkinter.Label(self.roomFrame)

        # Function Frame
        self.funcFrame = tkinter.Frame(self.mainFrame)
        self.codeEntry = tkinter.Entry(self.funcFrame)
        self.createBtn = tkinter.Button(self.funcFrame)
        self.joinBtn = tkinter.Button(self.funcFrame)

        self.setup()

    def setup(self):
        self.mainFrame.config(bg="#333")

        #==========================================================================================
        # room frame
        self.roomFrame.config(bg="#333")
        self.roomFrame.pack()
        
        # room listbox
        self.roomList.config(width=40,height=15,bd=0,bg="#333",fg="#fff",font=("Calibri",13),
                            selectmode="single",selectbackground="#33FF71")
        self.roomList.pack()

        # notification label
        self.notiLabel.config(bg="#333",fg="#21C653",font=("Calibri",20))
        self.notiLabel.pack(pady=10)


        #==========================================================================================
        # function frame
        self.funcFrame.config(bg="#333")
        self.funcFrame.pack()

        # room code entry
        self.codeEntry.config(width=30,font=("Calibri",13))
        self.codeEntry.grid(row=0,column=0,pady=10)

        # join button
        self.joinBtn.config(text="JOIN",font=("Calibri",13),width=30)
        self.joinBtn.grid(row=1,column=0,pady=10)

        # create button
        self.createBtn.config(text="CREATE",font=("Calibri",13),width=30)
        self.createBtn.grid(row=2,column=0,pady=10)

    def start(self):
        self.mainFrame.pack()

    def stop(self):
        self.mainFrame.pack_forget()

