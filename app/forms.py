from wtforms import Form, StringField, PasswordField, validators



class RegistrationForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    confirm = PasswordField('Repeat Password')
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])


class LoginForm(Form):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired()])

class CreateTeam(Form):
    name = StringField('name', [validators.DataRequired(), validators.Length(min=4, max=25)])
    show_description = StringField('show_description', [validators.DataRequired()])
    description = StringField('description', [validators.DataRequired()])
    country = StringField('country', [validators.DataRequired()])
    university = StringField('university', [validators.DataRequired()])
