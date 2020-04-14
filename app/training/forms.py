from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, FloatField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired


class CreateNewProlificProject(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    Description = StringField('Description', validators=[DataRequired()])
    no_of_workers = IntegerField('Number of Workers', validators=[DataRequired()])
    Fix_reward = FloatField('Fixed Reward', validators=[DataRequired()])
    completion_code = StringField('URL completion code', validators=[DataRequired()])
    create_button = SubmitField('CREATE A TASK')
    deactivate = SubmitField('DEACTIVATE THIS TASK')
