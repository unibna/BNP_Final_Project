import tkinter

class registerView:
    def __init__(self,master):
        self.mainFrame = tkinter.Frame(master)

        # description frame
        self.infoFrame = tkinter.Frame(self.mainFrame)
        self.nameLabel = tkinter.Label(self.infoFrame)
        self.notiLabel = tkinter.Label(self.infoFrame)

        # register frame
        self.registerFrame = tkinter.Frame(self.mainFrame)
        self.userLabel = tkinter.Label(self.registerFrame)
        self.userEntry = tkinter.Entry(self.registerFrame)
        self.emailLabel = tkinter.Label(self.registerFrame)
        self.emailEntry = tkinter.Entry(self.registerFrame)
        self.passLabel = tkinter.Label(self.registerFrame)
        self.passEntry = tkinter.Entry(self.registerFrame)
        self.confirmLabel = tkinter.Label(self.registerFrame)
        self.confirmEntry = tkinter.Entry(self.registerFrame)
        self.registerBtn = tkinter.Button(self.registerFrame)

        self.setup()

    def setup(self):
        self.mainFrame.config(bg="#333")

        # =====================================================================
        # Information Frame
        self.infoFrame.config(bg="#333")
        self.infoFrame.pack()
        # Name Label
        self.nameLabel.config(text="Gomoku",bg="#333",fg="pink",font=("Calibri",50))
        self.nameLabel.pack(pady=75)
        # Notification Label
        self.notiLabel.config(bg="#333",fg="#21C653",font=("Calibri",20))
        self.notiLabel.pack(pady=10)

        # =====================================================================
        # register Frame
        self.registerFrame.config(bg="#333")
        self.registerFrame.pack()
        # user label
        self.userLabel.config(text="username",bg="#333",fg="#fff",font=("Calibri",15))
        self.userLabel.grid(row=0,column=0)
        # user entry
        self.userEntry.config(width=30,font=("Calibri",15))
        self.userEntry.grid(row=0,column=1)
        # email label
        self.emailLabel.config(text="email",bg="#333",fg="#fff",font=("Calibri",15))
        self.emailLabel.grid(row=1,column=0)
        # email entry
        self.emailEntry.config(width=30,font=("Calibri",15))
        self.emailEntry.grid(row=1,column=1)
        # password label
        self.passLabel.config(text="password",bg="#333",fg="#fff",font=("Calibri",15))
        self.passLabel.grid(row=2,column=0)
        # password entry
        self.passEntry.config(width=30,font=("Calibri",15),show="●")
        self.passEntry.grid(row=2,column=1)
        # confirm label
        self.confirmLabel.config(text="confirm",bg="#333",fg="#fff",font=("Calibri",15))
        self.confirmLabel.grid(row=3,column=0)
        # confirm entry
        self.confirmEntry.config(width=30,font=("Calibri",15),show="●")
        self.confirmEntry.grid(row=3,column=1)

        # register button
        self.registerBtn.config(text="Register",width=14)
        self.registerBtn.grid(row=4,column=1,pady=20,sticky="w")

    def start(self):
        self.mainFrame.pack()

    def stop(self):
        self.mainFrame.pack_forget()