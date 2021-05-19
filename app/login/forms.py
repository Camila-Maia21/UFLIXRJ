from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, Email,  ValidationError

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired("Insira seu Nome")])
    password = PasswordField("Senha", validators=[DataRequired("Insira sua senha")])
    remember_me = BooleanField("Recordar registro")
    submit = SubmitField("Acessar")