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
    games_played = db.Column(db.Integer, nullable = False)
    receptions = db.Column(db.Integer, nullable = False)
    touchdowns = db.Column(db.Integer, nullable = False)
    passing_yards = db.Column(db.Integer, nullable = False)
    completions = db.Column(db.Integer, nullable = False)
    rushing_yards = db.Column(db.Integer, nullable = False)
    offensive_int = db.Column(db.Integer, nullable = False)
    defensive_int = db.Column(db.Integer, nullable = False)
    sacks = db.Column(db.Integer, nullable = False)
    tackles = db.Column(db.Integer, nullable = False)
    safety = db.Column(db.Integer, nullable = False)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))

