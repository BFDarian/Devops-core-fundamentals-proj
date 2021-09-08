from application import db

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(40))
    team_stadium = db.Column(db.String(40))
    team_location = db.Column(db.String(50))
    team_owner = db.Column(db.String(40))
    capacity = db.Column(db.Integer)
    players = db.relationship('Player', backref = 'team')

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player_name = db.Column(db.String(50))
    position = db.Column(db.String(30))
    height = db.Column(db.Integer)
    DoB = db.Column(db.DateTime)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    stats = db.relationship('Stats', backref = 'player')

class Stats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    games_played = db.Column(db.Integer)
    receptions = db.Column(db.Integer)
    touchdowns = db.Column(db.Integer)
    passing_yards = db.Column(db.Integer)
    completions = db.Column(db.Integer)
    rushing_yards = db.Column(db.Integer)
    offensive_int = db.Column(db.Integer)
    defensive_int = db.Column(db.Integer)
    sacks = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    safety = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))

