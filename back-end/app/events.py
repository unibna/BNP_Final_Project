from flask_socketio import emit, join_room, leave_room, disconnect, rooms, ConnectionRefusedError
from flask_login import current_user, login_user, logout_user
from flask import request, session, g
from app import socketio, app
from app.models import User
from app.forms import LoginForm
import werkzeug

# store game maze and list of users
roomdata = {}
# store roomid that user joined
userdata = {}

def login(data):
	if current_user.is_authenticated:
		return make_response("Login form success", 200)

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

def valid_move(data, x, y):
	size = app.config['MAZESIZE']
	if 0 <= x < size and 0 <= y < size:
		if data[x][y] == 0:
			return True
		else:
			return False
	else:
		return False

def leave():
	global roomdata
	global userdata

	# if user is in a room
	if current_user.username in userdata:
		roomid = userdata[current_user.username]
		# if room exists
		if roomid in roomdata:
			roomdata[roomid]['users'].remove(current_user.username)
			# if all users exitted, delete room
			if len(roomdata[roomid]['users']) == 0:
				roomdata.pop(roomid, None)
			leave_room(roomid)
			emit('message', {'data': 'User is leaving the room', 'code':1})
			userdata.pop(current_user.username, None)
		else:
			emit('message', {'data': 'Room is not created', 'code':0})
	else:
		emit('message', {'data': 'User is not currently in a room', 'code':0})



@socketio.on('connect')
def connect():
	print('[*] connect')
	data = werkzeug.datastructures.ImmutableMultiDict({
		'username': request.headers.get('Username'),
		'password': request.headers.get('Password')
		})
	if current_user.is_anonymous:
		# login successfully
		if login(data):
			emit('message response', {'data': 'Connected', 'code':0})
		else:
			disconnect()
			raise ConnectionRefusedError('unauthorized!')

@socketio.on('message')
def text(message):
	"""
	Receive text message from client
	"""
	emit('message', {'data': "ye man i've got it, " + current_user.username})


@socketio.on('create room')
def create_room(message):
	"""
	Create a room, join default user in
	"""
	global roomdata
	global userdata

	roomid = message['data']
	# if roomid is not taken 
	if roomid not in roomdata:
		# and user is not in another room
		if current_user.username not in userdata:
			# initialize the maze
			size = app.config['MAZESIZE']
			maze = [[0] * size for i in range(size)]

			roomdata[roomid] = {"users":[current_user.username], "maze":maze}
			userdata[current_user.username] = roomid

			join_room(roomid)
			emit('message', {'data': 'User has created room ' + roomid, 'code':1}, room=roomid)
		else:
			emit('message', {'data': 'User is already in another room', 'code':0}, broadcast=False)
	else:
		emit('message', {'data': 'Room is already created', 'code':0}, broadcast=False)


@socketio.on('join')
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
				emit('message', {'data': 'Room is joined successfully', 'code':1})
			else:
				emit('message', {'data': 'User is already in another room', 'code':0})
		else:
			emit('message', {'data': 'Room is full', 'code':0})
	else:
		emit('message', {'data': 'Room is not created', 'code':0})

@socketio.on('move')
def move(message):
	"""
	Receive game move from client, log move, check winner
	"""
	global roomdata
	global userdata

	if current_user.username not in userdata:
		emit('message', {'data': 'User is not currently in a room', 'code': 0})
		return

	roomid = userdata[current_user.username]
	x = int(message['x'])
	y = int(message['y'])
	

	if valid_move(roomdata[roomid]['maze'], x, y):
		print("Room " + roomid + " : " + current_user.username + " made move " + str(x) + " " + str(y))
		symbol = 'O'
		roomdata[roomid]['maze'][x][y] = symbol
		displaymaze(roomdata[roomid]['maze'])
		emit('message', {'data': 'Valid move', 'code':1})
	else:
		emit('message', {'data': 'Invalid move!', 'code':0})

@socketio.on('leave')
def user_leave(message):
	leave()

@socketio.on('disconnect')
def disconnect():
	leave()
	logout_user()
