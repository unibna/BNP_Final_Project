import tkinter
from tkinter import messagebox
from login import loginView
from register import registerView
from lobby import lobbyView
from game import gomoku

class View:
    def __init__(self):
        self.master = tkinter.Tk(className="Gomoku")
        self.Login = loginView(self.master)
        self.Register = registerView(self.master)
        self.Lobby = lobbyView(self.master)
        self.Game  = gomoku(self.master)
        
        self.setup()

    def setup(self):
        self.master.geometry("450x600")
        self.master.config(bg="#333")  

        self.Login.start()
        self.Lobby.stop()
        
    def start(self):
        # self.Game.start()
        self.Login.start()
        self.master.mainloop()
