from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, Email

class PropertyForm(FlaskForm):
    title = StringField('Property Title',validators=[DataRequired()])
    no_of_rooms = StringField('No. of Rooms',validators=[DataRequired()])
    no_of_bathrooms = StringField('No. of Bathrooms',validators=[DataRequired()])
    location = StringField('Location',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    type_ = SelectField(u'Property Type', choices=[('House', 'House'), ('Apartment', 'Apartment')])
    description = TextAreaField('Description',validators=[DataRequired()])
    photo = FileField('Photo',validators=[
        FileRequired(),
        FileAllowed(['jpg','png','.jpeg','Images only!'])
    ])

