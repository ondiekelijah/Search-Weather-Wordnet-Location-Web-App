from wtforms import (
    StringField,
    TextAreaField,
)
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp



class Questions(FlaskForm):
    body = StringField(
        validators=[
            InputRequired(),
            Length(3, 100, message="Question format is invalid !"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Questions must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )

class Weather(FlaskForm):
    place = StringField(
        validators=[
            InputRequired(),
            Length(3, 100, message="City name format is invalid !"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "City names must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )
class Wordnet(FlaskForm):
    word = StringField(
        validators=[
            InputRequired(),
            Length(3, 100, message="Word format is invalid !"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Words must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )

class Location(FlaskForm):
    address = StringField(
        validators=[
            InputRequired(),
            Length(3, 100, message="Word format is invalid !"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Words must have only letters, " "numbers, dots or underscores",
            ),
        ]
    )



