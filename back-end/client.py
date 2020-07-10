import socketio
import requests
import sys

sio = socketio.Client()

# Registation is done via http
def register():
	url = "http://localhost:5000/register"
	payload = {"username":"haole", "email":"hello@gmail.com", "password":"leanhhao" }

	print(requests.post(url, data=payload).text)

# Login + connect to socketio server
def connect(username, password):
	header = {'username': username, 'password':password}    
	sio.connect('http://localhost:5000', headers=header)

def create_room(roomid):
	sio.emit('create room', {'data': roomid})

def join(roomid):
	sio.emit('join', {'data':roomid})

def leave():
	sio.emit('leave', {})

def makemove(x, y):
	sio.emit('move', {'x':x, 'y': y})

@sio.on('message')
def response(message):
    print(message)

	