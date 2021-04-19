from wtforms import Form, PasswordField, StringField

class LoginForm(Form):
	username = StringField('Username')
	password = PasswordField('Password')