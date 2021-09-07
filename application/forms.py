from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, ValidationError

class AddTeam(FlaskForm):
    team_name = StringField('Team Name', validators = [DataRequired(message = "Field cannot be empty")])
    stadium_name = StringField('Stadium name')
    team_location = StringField('Team location', validators = [DataRequired(message = "Field cannot be empty")])
    team_owner = StringField('Team Owner')
    capacity = IntegerField('Capacity')
    submit = SubmitField('Add Team')


class AddPlayer(FlaskForm):
    player_name = StringField('Player Name', validators = [DataRequired(message = "Field cannot be empty")])
    position = SelectField('Player Position', 
        choices = [("QB","QB"), ("RB","RB"), ("OL","OL"), ("TE","TE"), ("WR","WR"), ("DL","DL"), ("LB","LB"), ("DB","DB"), ("K","K"), ("P","P")])
    height = IntegerField('Player Height(cm)')
    DoB = DateField('Date of Birth') 
    team = SelectField('Team', choices=[])
    submit = SubmitField('Add Player')


class AddStats(FlaskForms):
   games_played = IntegerField('Games Played', validators = [DataRequired(message = "Field cannot be empty")])
   receptions = IntegerField('Receptions', validators = [DataRequired(message = "Field cannot be empty")])
   touchdowns = IntegerField('Touchdowns', validators = [DataRequired(message = "Field cannot be empty")])
   pass_yards = IntegerField('Passing Yards', validators = [DataRequired(message = "Field cannot be empty")])
   completions = IntegerField('Completions', validators = [DataRequired(message = "Field cannot be empty")])
   rush_yards = IntegerField('Rushing Yards', validators = [DataRequired(message = "Field cannot be empty")])
   off_int = IntegerField('Offensive Interceptions', validators = [DataRequired(message = "Field cannot be empty")])
   def_int = IntegerField('Defensive Interceptions', validators = [DataRequired(message = "Field cannot be empty")]) 
   sacks = IntegerField('Sacks', validators = [DataRequired(message = "Field cannot be empty")])
   tackles = IntegerField('Tackles', validators = [DataRequired(message = "Field cannot be empty")])
   safety = IntegerField('Safety', validators = [DataRequired(message = "Field cannot be empty")])
   submit = SubmitField('Add Player Statistics')


class SelectTeam(FlaskForm):
    teamID = SelectField('Team', choices = [])
    submit = SubmitField('Choose Team')


class SelectPlayer(FlaskForm):
    playerID = SelectField('Player', choices = [])
    submit = SubmitField('Choose Player')