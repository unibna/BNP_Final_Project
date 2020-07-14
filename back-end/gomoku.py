from app import app, socketio
app.config['DEBUG'] = True

if __name__ == '__main__':
	socketio.run(app)
