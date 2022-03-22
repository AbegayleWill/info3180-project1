
# Global Imports
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed

# Class


class PropertyForm(FlaskForm):
    # Attributes
    p_title = StringField('Property Title', validators=[DataRequired()])
    p_description = TextAreaField('Description', validators=[DataRequired()])
    rooms = StringField('No. of Rooms', validators=[DataRequired()])
    bathrooms = StringField('No. of Bathrooms', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    p_type = SelectField('Property Type', choices=[
                         ('House', 'House'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'])])

 
