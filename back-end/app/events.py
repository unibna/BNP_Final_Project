from flask_socketio import emit, join_room, leave_room, disconnect, rooms, ConnectionRefusedError
from flask_login import current_user, login_user, logout_user
from flask import request, session, g
from app import socketio, app
from app.models import User
from app.forms import LoginForm
from app.logic import logic
from app import db
import werkzeug
import functools

# store game maze and list of users
roomdata = {}
# store roomid that user joined
userdata = {}

def authenticated_only(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped

def login(data):
	if current_user.is_authenticated:
		return True

	form = LoginForm(data)
	if form.validate():
		print(form.username.data, form.password.data)
		user = User.query.filter_by(username=form.username.data).first()
		if user is None or not user.check_password(form.password.data):
			print("[*] Socketio login failed, invalid username or password")
			return False
		login_user(user)
		return True
	else:
		print("[*] Socketio login faied, invalid form")
		return False

def displaymaze(data):
	for i in range(app.config['MAZESIZE']):
		print(data[i])

def valid_move(roomid, x, y):
	if roomdata[roomid]['turn'] != roomdata[roomid]['users'].index(current_user.username):
		print(roomdata[roomid]['turn'],roomdata[roomid]['users'].index(current_user.username))
		return -1
	
	return roomdata[roomid]['maze'].check(x,y,roomdata[roomid]['turn'] + 1)

def restart_room(roomid):
	roomdata[roomid]['maze'].reset()
	roomdata[roomid]['turn'] ^= 1

def update_user_score():
	user = User.query.filter_by(username=current_user.username).first()
	user.update_score()
	db.session.commit()
	print("Score updated!!")

def leave():
	global roomdata
	global userdata

	if current_user.is_anonymous:
		return
	# if user is in a room
	if current_user.username in userdata:
		roomid = userdata[current_user.username]
		# if room exists
		if roomid in roomdata:
			print("LEAVE ", roomdata[roomid]['users'])
			emit('leave', {'data': 'User is leaving the room','username':current_user.username, 'code':1},broadcast=True)
			# if all users exitted, delete room
			roomdata[roomid]['users'].remove(current_user.username)
			if len(roomdata[roomid]['users']) == 0:
				print('DELETING ROOM')
				roomdata.pop(roomid, None)
			leave_room(roomid)
			userdata.pop(current_user.username, None)
			restart_room(roomid)
		else:
			emit('leave', {'data': 'Room is not created','username':current_user.username,'code':0})
	else:
		emit('leave', {'data': 'User is not currently in a room','username':current_user.username, 'code':0})

@socketio.on('connect')
def connect():
	print('[*] connect')
	socketio.emit('response connect',{'data':'Connected'})

@socketio.on('login')
@authenticated_only
def handleLogin(message):
	print("Login ", message['username'])
	data = werkzeug.datastructures.ImmutableMultiDict({
	'username': message['username'],
	'password': message['password']
	})
	if current_user.is_anonymous:
		# login successfully
		if login(data):
			print("Login successfully")
			return {'data': 'Login successfully', 'code':1}
		else:
			print("Login failed")
			return {'data': 'Login failed', 'code':0}
			# raise ConnectionRefusedError('unauthorized!')

@socketio.on('message')
@authenticated_only
def text(message):
	"""
	Receive text message from client
	"""
	emit('message', {'data': "ye man i've got it, " + current_user.username})

@socketio.on('create room')
@authenticated_only
def create_room(message):
	"""
	Create a room, join default user in
	"""
	global roomdata
	global userdata

	roomid = message['data']
	# if roomid iens not tak 
	if roomid not in roomdata:
		# and user is not in another room
		if current_user.username not in userdata:
			# initialize the maze
			size = app.config['MAZESIZE']
			maze = [[0] * size for i in range(size)]

			roomdata[roomid] = {"users":[current_user.username], "maze": logic(maze), 'turn': 0}
			userdata[current_user.username] = roomid

			join_room(roomid)
			socketio.emit('user join',{'username':roomdata[roomid]['users'],'code':1})
			return {'data': 'User has created room ' + roomid, 'code':1}
		else:
			return {'data': 'User is already in another room', 'code':0}
	else:
		return {'data': 'Room is already created', 'code':0}

@socketio.on('join')
@authenticated_only
def user_join(message):

	"""
	Join user in already created room
	"""
	global roomdata
	global userdata

	roomid = message['data']
	# if room exists
	if roomid in roomdata:
		# and room is not full
		if len(roomdata[roomid]['users']) < 2:
			# if user is not in another room
			if current_user.username not in userdata:
				roomdata[roomid]['users'].append(current_user.username)
				userdata[current_user.username] = roomid
				join_room(roomid)
				socketio.emit('user join',{'username':roomdata[roomid]['users'],'code':1})
				return {'data': 'Room is joined successfully', 'code':1}
			else:
				return {'data': 'User is already in another room', 'code':0}
		else:
			return {'data': 'Room is full', 'code':0}
	else:
		return {'data': 'Room is not created', 'code':0}

@socketio.on('move')
@authenticated_only
def move(message):
	"""
	Receive game move from client, log move, check winner
	"""
	global roomdata
	global userdata

	if current_user.username not in userdata:
		return {'data': 'User is not currently in a room', 'code': 0}

	roomid = userdata[current_user.username]
	x = int(message['x'])
	y = int(message['y'])

	print(message)
	# message response: data-player-code
	check = valid_move(roomid,x,y)
	if check == -1:
		socketio.emit('response move',{'data':'Invalid Move','coord':(x,y),'username':current_user.username,'code':0})
	elif check == 1:
		socketio.emit('response move',{'data':'Win','coord':(x,y),'username':current_user.username,'code':1})
		print(current_user.username)
		update_user_score()
		restart_room(roomid)
	elif check == 0:
		socketio.emit('response move',{'data':'Valid Move','coord':(x,y),'username':current_user.username,'code':1})
		roomdata[roomid]['turn'] ^= 1

@socketio.on('leave')
@authenticated_only
def user_leave(message):
	print(message)
	leave()

@socketio.on('disconnect')
def disconnect():
	leave()
	logout_user()
