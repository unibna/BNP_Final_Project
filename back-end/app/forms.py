from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])


	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		print('[************] validating username')
		if user is not None:
			print('[***********] duplicate username')
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(username=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email.')	