from wtforms import Form, StringField, PasswordField, validators

class RegistrationForm(Form):
    username = StringField('Username', validators=[validators.Length(min=4, max=12)])
    password = PasswordField('New Password', validators=[
        validators.DataRequired(),
        validators.Length(min=4, max=12),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

    def __repr__(self):
        print(self.username or None)

class LoginForm(Form):
    username = StringField('Username', validators=[validators.Length(min=4, max=12)])
    password = PasswordField('Password', validators=[
        validators.DataRequired(),
        validators.Length(min=4, max=12),
    ])