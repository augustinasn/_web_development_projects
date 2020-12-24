from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField

class UploadFile(FlaskForm):
    picture = FileField("Dokumentas: ",
                        validators=[FileAllowed(["jpg", "png", "pdf"])])
    
    submit = SubmitField("Nuskaityti!")    

