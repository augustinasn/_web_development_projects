from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SubmitField, IntegerField, FileField, PasswordField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp

class SearchForm(FlaskForm):
    item_name = StringField("Search String", validators=[DataRequired(), Length(max=50)], render_kw={"placeholder": "Item you're looking for..."})
    submit = SubmitField("Search")

class AddImageForm(FlaskForm):
    picture = FileField("Picture: ", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Next")     

class AddItemForm(FlaskForm):
    item_name = StringField("Item Name: ", validators=[DataRequired(), Length(min=3, max=100)])
    box_number = IntegerField("Box Number: ", validators=[DataRequired(), NumberRange(min=0, max=99)])
    submit = SubmitField("Add")

class LoginForm(FlaskForm):
    username = StringField("User name", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")