from app import app
from app.forms import LoginForm, RegistrationForm
from flask import request, render_template, make_response
from flask_login import current_user, login_user
from app.models import User
from app import db	
from flask_socketio import disconnect, emit
from app import events
import functools


@app.route('/')
@app.route('/index')
def index():
	return "hiiii"

@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		make_response("Already authenticated", 200)
	form = RegistrationForm(request.form)
	if request.method == 'POST':
		if form.validate_on_submit():
			user = User(username=form.username.data, email=form.email.data)
			user.set_password(form.password.data)
			db.session.add(user)
			db.session.commit()
			print("Registration successfully")
			return make_response("Registration successfully", 200)
		
		print("Registration form validation failed")
		return make_response("Registration form validation failed", 400)

	return make_response("Method not allowed", 405)





