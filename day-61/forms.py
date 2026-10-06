from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired(), Length(1, 64), Email(message='Invalid email address')])
    username = StringField('Username', validators = [DataRequired(), Length(min=8, max=30, message= 'Username is too long.')])
    password = PasswordField('Password', validators = [DataRequired(), Length(min=8, message= 'Password is too short.')])
    submit = SubmitField('Login')