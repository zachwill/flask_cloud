"""
WTForms Documentation:    http://wtforms.simplecodes.com/
Flask WTForms Patterns:   http://flask.pocoo.org/docs/patterns/wtforms/
Flask-WTF Documentation:  http://packages.python.org/Flask-WTF/

Forms for your application can be stored in this file.
"""

from flaskext.wtf import Form, SelectField, SubmitField, TextField, Required

class EpaForm(Form):
    """Form for querying the EPA APIs."""
    location = TextField('Location', validators=[Required()])
    submit = SubmitField('Submit')
    q = SelectField(choices=[
        ('pcs', "Which facilities can pollute public water sources?"),
        ('radinfo', "Where's the closest radiation facility?"),
    ])
