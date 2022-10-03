from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# FORM FOR ADDING TO DOS
class CreateForm(FlaskForm):
    todo = StringField("To Do Item:", validators=[DataRequired()])
    submit = SubmitField("Add To Do")

# FORM FOR UPDATING TO DOS
class UpdateForm(FlaskForm):
    todo = StringField("To Do Item:", validators=[DataRequired()])
    submit  = SubmitField("Update To Do")

# FORM FOR DELETING TO DOS
class DeleteForm(FlaskForm):
    submit = SubmitField("Delete")