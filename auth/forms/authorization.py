from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': 'Введите почту'})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={'placeholder': 'Введите пароль'})
    remember = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')