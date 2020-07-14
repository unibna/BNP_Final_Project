import tkinter

class loginView:
    def __init__(self,master):
        self.mainFrame = tkinter.Frame(master)

        # description frame
        self.infoFrame = tkinter.Frame(self.mainFrame)
        self.nameLabel = tkinter.Label(self.infoFrame)
        self.notiLabel = tkinter.Label(self.mainFrame)

        # login frame
        self.loginFrame = tkinter.Frame(self.mainFrame)
        self.userLabel = tkinter.Label(self.loginFrame)
        self.userEntry = tkinter.Entry(self.loginFrame)
        self.passLabel = tkinter.Label(self.loginFrame)
        self.passEntry = tkinter.Entry(self.loginFrame)
        self.loginBtn = tkinter.Button(self.loginFrame)

        # register
        self.registerBtn = tkinter.Button(self.loginFrame)

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
        self.notiLabel.pack(pady=5)

        # =====================================================================
        # Login Frame
        self.loginFrame.config(bg="#333")
        self.loginFrame.pack()
        # user label
        self.userLabel.config(text="username",bg="#333",fg="#fff",font=("Calibri",15))
        self.userLabel.grid(row=0,column=0)
        # user entry
        self.userEntry.config(width=30,font=("Calibri",15))
        self.userEntry.grid(row=0,column=1)
        # password label
        self.passLabel.config(text="password",bg="#333",fg="#fff",font=("Calibri",15))
        self.passLabel.grid(row=1,column=0)
        # password entry
        self.passEntry.config(width=30,font=("Calibri",15),show="●")
        self.passEntry.grid(row=1,column=1)
        # login button
        self.loginBtn.config(text="Login",width=14)
        self.loginBtn.grid(row=2,column=1,pady=20,sticky="w")

        # =====================================================================
        # register
        self.registerBtn.config(text='Register',width=14)
        self.registerBtn.grid(row=3,column=1,sticky="w")

    def start(self):
        self.mainFrame.pack()

    def stop(self):
        self.mainFrame.pack_forget()