from flask import render_template, request, url_for, redirect
from application import app, db
from application.forms import AddTeam, AddPlayer, AddStats
from application.models import Team, Player, Stats

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/teams')
def teams():
    nflTeams = Team.query.all()
    return render_template('teams.html', nflTeams = nflTeams)

@app.route('/teamPlayers-<int:teamid>')
def teamPlayer(teamid):
    nflPlayer = Player.query.filter_by(team_id = teamid)
    return render_template('teamPlayers.html', nflPlayer = nflPlayer)

@app.route('addTeam', methods=['GET','POST'])
def addTeam():
    form = AddTeam()
    if request.method =='POST':
        name = form.team_name.data
        stadium = form.stadium_name.data
        loc = form.team_location.data
        owner = form.team_owner.data
        capacity = form.capacity.data
        team = Team(team_name = name, stadium_name = stadium, team_location = loc, team_owner = owner, capacity= capacity)
        db.session.add(team)
        db.session.commit()
        newTeam = Team.query.filter_by(team_name = name)
        AddPlayer().team.choices.append((newTeam.id,newTeam.team_name))
    return render_template('addTeam.html', form = form)

@app.route('addPlayer', methods=['GET'.'POST'])
def addPlayer():
    form = AddPlayer()
    if request.method == 'POST':
        name = form.player_name.data
        position = form.position.data
        height = form.height.data
        dob = form.DoB.data
        team = form.team.data
    




    



