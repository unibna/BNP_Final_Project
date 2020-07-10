import tkinter

class loginView:
    def __init__(self):
        # master brand
        self.master = tkinter.Tk(className=" HLC Gomoku")

        #==========================================================================================
        # descript frame
        self.desFrame = tkinter.Frame(self.master)

        self.descript = tkinter.Label(self.desFrame)
        self.noti = tkinter.Label(self.desFrame)

        #==========================================================================================
        # login frame
        self.loginFrame = tkinter.Frame(self.master)

        self.userLabel = tkinter.Label(self.loginFrame)
        self.userEntry = tkinter.Entry(self.loginFrame)

        self.passLabel = tkinter.Label(self.loginFrame)
        self.passEntry = tkinter.Entry(self.loginFrame)

        self.loginBtn = tkinter.Button(self.loginFrame)
        
        # set up all
        self.setView()
        
    def setView(self):
        # master
        self.master.geometry("450x350")
        self.master.config(bg="#333")
        
        # description Frame
        self.desFrame.config(bg="#333")
        self.desFrame.pack()
        # description Label
        self.descript.config(text="Gomoku",bg="#333",fg="pink",font=("Calibri",50))
        self.descript.pack()
        # noti Label
        self.noti.config(text="Login successfully",bg="#333",pady=20,font=("Calibri",25))
        self.noti.pack()

        # login Frame
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
        self.passEntry.config(width=30,font=("Calibri",15),show="*")
        self.passEntry.grid(row=1,column=1)
        # login button
        self.loginBtn.config(text="Login",width=14,command=self.verify)
        self.loginBtn.grid(row=2,column=1,pady=20,sticky="w")
        
    def start(self):
        self.master.mainloop()

    def verify(self):
        username = self.userEntry.get()
        password = self.passEntry.get()
        print(f"{username} {password}")
        return username,password

if __name__ == "__main__":
    v = loginView()
    v.start()