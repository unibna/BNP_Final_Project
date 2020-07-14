import socketio
from view import View
from tkinter import messagebox
import requests

sio = socketio.Client()
form = View()
username = None
chess = None

def connect():
    sio.connect('http://localhost:5000')

def open_register():
    # change register form
    form.Login.stop()
    form.Register.start()

def open_game():
    # open game window
    form.Lobby.joinBtn['state'] = 'disable'
    form.Lobby.createBtn['state'] = 'disable'
    form.Game.start()

def close_form():
    print('<Gomoku> See you later!')
    form.master.destroy()

def close_game():
    print('<Gomoku Game> Close Game')
    form.Game.stop()
    form.Lobby.joinBtn['state'] = 'normal'
    form.Lobby.createBtn['state'] = 'normal'
    sio.emit('leave',{})

def login():
    global username,chess
    # get info 
    username = form.Login.userEntry.get()
    password = form.Login.passEntry.get()

    # check if input is empty
    if username == "" or password == "":
        form.Login.notiLabel['text'] = "Please Complete!"
        return
    
    # request to login
    data = sio.call('login',{'username':username,'password':password})
    print(data)
    if data['code']:
        username = form.Login.userEntry.get()
        chess = 1
        form.Login.stop()
        form.Lobby.start()
    else:
        form.Login.notiLabel['text'] == 'Login failed!'

def register():
    global chess,username

    # get info from register form
    user = form.Register.userEntry.get()
    email = form.Register.emailEntry.get()
    password = form.Register.passEntry.get()
    confirm = form.Register.confirmEntry.get()

    # check if input is empty or password and confirm are not the same
    if confirm != password or user == "" or password == "" or confirm == "":
        form.Register.notiLabel['text'] = 'Please Complete!'
    else:
        # request to server
        url = "http://localhost:5000/register"
        payload = {"username":user, "email":email, "password":password}

        print("Getting response")
        response = requests.post(url, data=payload).text
        print(response)
        if response == "Registration form validation failed":
            # response fail
            form.Register.notiLabel['text'] = 'Register Failed'
        elif response == "Registration successfully":
            username = form.Register.userEntry.get()
            chess = 1
            # open lobby form
            form.Register.stop()
            form.Lobby.start()
        
def join():
    code = form.Lobby.codeEntry.get()
    data = sio.call('join',{'data':code})
    if data['code']:
        form.Lobby.notiLabel['text'] = 'You are in a room'
        open_game()
    else:
        form.Lobby.notiLabel['text'] = 'Join unsuccessfully!'

def create():
    code = form.Lobby.codeEntry.get()
    # cannot create empty code
    if code != "":
        data = sio.call('create room',{'data':code})
        if data['code']:
            form.Lobby.notiLabel['text'] = 'You are in a room'
            open_game()
            return
    form.Lobby.notiLabel['text'] = 'Create unsuccessfully!'

def make_move(mEvent):
    row, col = form.Game.toRow(mEvent.x - 10, mEvent.y - 10)
    sio.emit('move',{'x': row, 'y':col})

def bindFunc():
    # Master Bind
    form.master.protocol('WM_DELETE_WINDOW',close_form)

    # Login Bind
    form.Login.loginBtn['command'] = login
    form.Login.registerBtn['command'] = open_register
    # form.Login.mainFrame.bind('<Enter>',login)

    # Register Bind
    form.Register.registerBtn['command'] = register
    # form.Register.mainFrame.bind('<Enter>',register)

    # Lobby Bind
    form.Lobby.joinBtn['command'] = join
    form.Lobby.createBtn['command'] = create
    # form.Lobby.mainFrame.bind('<Enter>',join)

    # Game Bind
    form.Game.master.protocol('WM_DELETE_WINDOW',close_game)
    form.Game.master.bind('<Double-Button-1>',make_move)
    form.Game.exitBtn['command'] = close_game

def run():
    bindFunc()
    connect()
    form.start()

@sio.on('response connect')
def response_connect(message):
    if message['data'] == 'Connected':
        form.start()

@sio.on('user join')
def player_join(message):
    print(message)
    if message['code']:
        for name in message['username']:
            if name == username:
                form.Game.player_1_Label['text'] = name
            else:
                form.Game.player_2_Label['text'] = name

@sio.on('leave')
def response_restart(message):
    print(message,username)
    if message['code']:
        form.Game.restart()
        form.Game.player_2_Label['text'] = ''

@sio.on('response move')
def response_move(message):
    print(message,username)
    if message['code']:
        if message['username'] == username:
            form.Game.draw(chess,message['coord'])
        else:
            other_chess = 1
            if chess == 1:
                other_chess = 2
            form.Game.draw(other_chess,message['coord'])
        # if win, display
        if message['data'] == 'Win':
            form.Game.winner_Label['text'] = message['username']
            form.Game.restart()
    else:
        return


if __name__ == "__main__":
    run()

