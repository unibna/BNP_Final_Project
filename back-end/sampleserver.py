from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'urmomisgay'
socketio = SocketIO(app)

@app.route('/')
def index():
    print("Incoming connection")

@socketio.on('my event')
def test_message(message):
    print(message)
    emit('my response', {'data':message['data']})

@socketio.on('my broadcase event')
def test_message(message):
    print(message)
    emit('my response', {'data':message['data']}, broadcase=True)

@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


if __name__ == "__main__":
    socketio.run(app, port=5000)
