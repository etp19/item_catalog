from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required, Email, InputRequired, Length, AnyOf, URL


# class SignupForm(FlaskForm):
#     name = TextField(u'Your name', validators=[Required()])
#     password = TextField(u'Your favorite password', validators=[Required()])
#     email = TextField(u'Your email address', validators=[Email()])
#     birthday = DateField(u'Your birthday')
#
#     a_float = FloatField(u'A floating point number')
#     a_decimal = DecimalField(u'Another floating point number')
#     a_integer = IntegerField(u'An integer')
#
#     now = DateTimeField(u'Current time',
#                         description='...for no particular reason')
#     sample_file = FileField(u'Your favorite file')
#     eula = BooleanField(u'I did not read the terms and conditions',
#                         validators=[Required('You must agree to not agree!')])
#
#     submit = SubmitField(u'Signup')


class RestaurantForm(FlaskForm):
    """Create WTForm to add restaurants"""
    name = StringField('Name', validators=[InputRequired()])
    phone = StringField('Phone #', validators=[InputRequired()])
    email = StringField('E-Mail', validators=[InputRequired(),
                                              Email("This field requires a valid email address")])
    course = SelectField(u'Course', choices=[('American', 'American'), ('Mexican', 'Mexican'),
                                             ('India', 'India'), ('Mediterranean', 'Mediterranean'),
                                             ('Caribbean', 'Caribbean'), ('Asia', 'Asia'),
                                             ('Mix', 'Mix')], validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired(), Length(min=5, max=200)])
    website = StringField('Website', validators=[InputRequired(),
                                                 URL(require_tld=True, message="Enter a valid URL")])
    street = StringField('Street', validators=[InputRequired()])
    city = StringField('City', validators=[InputRequired()])
    state = StringField('State', validators=[InputRequired()])
    zip_code = StringField('Zip Code', validators=[InputRequired()])
