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


@app.route('/teamPlayers/<int:teamid>')
def teamPlayers(teamid):
    nflPlayer = Player.query.filter_by(team_id = teamid)
    return render_template('teamPlayers.html', nflPlayer = nflPlayer)


@app.route('/playerStats/<int:playerid>')
def playerStats(playerid):
    player = Player.query.filter_by(id = playerid).first()
    name = player.player_name
    nflPlayerStat = Stats.query.filter_by(player_id = playerid).first()
    return render_template('playerStats.html', nflPlayerStat = nflPlayerStat, name = name)


@app.route('/addTeam', methods=['GET','POST'])
def addTeam():
    form = AddTeam()
    if request.method =='POST':
        team = Team(team_name = form.team_name.data, 
                    team_stadium = form.stadium_name.data, 
                    team_location = form.team_location.data, 
                    team_owner = form.team_owner.data, 
                    capacity= form.capacity.data)
        db.session.add(team)
        db.session.commit()
        return redirect(url_for('teams'))
    return render_template('addTeam.html', form = form)


@app.route('/addPlayer', methods=['GET','POST'])
def addPlayer():
    form = AddPlayer()
    teamSelect = Team.query.all()
    for team in teamSelect:
        form.team.choices.append((team.id,team.team_name))
    if request.method == 'POST':
        player = Player(player_name = form.player_name.data, 
                        position = form.position.data, 
                        height = form.height.data, 
                        DoB = form.DoB.data, 
                        team_id = form.team.data)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('addStats', playerid = player.id ))
    return render_template('addPlayer.html', form = form)


@app.route('/addStats/<int:playerid>', methods=['GET','POST'])
def addStats(playerid):
    form = AddStats()
    if request.method =='POST':
        stat = Stats(games_played = form.games_played.data, 
                    receptions = form.receptions.data, 
                    touchdowns = form.touchdowns.data, 
                    passing_yards = form.pass_yards.data, 
                    completions = form.completions.data, 
                    rushing_yards = form.rush_yards.data, 
                    offensive_int = form.off_int.data,
                    defensive_int = form.def_int.data, 
                    sacks = form.sacks.data, 
                    tackles = form.tackles.data, 
                    safety = form.safety.data, 
                    player_id = playerid)
        db.session.add(stat)
        db.session.commit()
        return redirect(url_for('teams'))
    return render_template('addStats.html', form = form)


@app.route('/updateTeam/<int:teamid>', methods = ['GET', 'POST'])
def updateTeam(teamid):
    form = AddTeam()
    team = Team.query.get(teamid)
    if form.validate_on_submit():
        team.team_name = form.team_name.data
        team.team_stadium = form.stadium_name.data
        team.team_location = form.team_location.data
        team.team_owner = form.team_owner.data
        team.capacity = form.capacity.data
        db.session.commit()
        return redirect(url_for('teams'))
    elif request.method == 'GET':
        form.team_name.data = team.team_name
        form.stadium_name.data = team.team_stadium
        form.team_location.data = team.team_location
        form.team_owner.data = team.team_owner
        form.capacity.data = team.capacity
    return render_template('updateTeam.html', form = form)  


@app.route('/updatePlayer/<int:playerid>', methods = ['GET', 'POST'])
def updatePlayer(playerid):
    form = AddPlayer()
    player = Player.query.get(playerid)
    teamSelect = Team.query.all()
    for team in teamSelect:
        form.team.choices.append((team.id,team.team_name))
    if form.validate_on_submit():
        player.player_name = form.player_name.data
        player.position = form.position.data
        player.height = form.height.data
        player.DoB = form.DoB.data
        player.team_id = form.team.data
        db.session.commit()
        return redirect(url_for('teams'))
    elif request.method == 'GET':
        form.player_name.data = player.player_name
        form.position.data = player.position
        form.height.data = player.height
        form.DoB.data = player.DoB
        form.team.data = player.team_id
    return render_template('updatePlayer.html', form = form)


@app.route('/updateStats/<int:playerid>', methods=['GET','POST'])
def updateStats(playerid):
    form = AddStats()
    stat = Stats.query.filter_by(player_id=playerid).first()
    stat1 = Stats.query.get(stat.id)
    print(stat.id, stat.games_played)
    if request.method == 'POST':
        print('validate')
        stat1.games_played = form.games_played.data
        stat1.receptions = form.receptions.data
        stat1.touchdowns = form.touchdowns.data
        stat1.passing_yards = form.pass_yards.data
        stat1.completions = form.completions.data
        stat1.rushing_yards = form.rush_yards.data
        stat1.offensive_int = form.off_int.data
        stat1.defensive_int = form.def_int.data
        stat1.sacks = form.sacks.data
        stat1.tackles = form.tackles.data
        stat1.safety = form.safety.data
        db.session.commit()
        print(stat.id, stat.games_played)
        return redirect(url_for('teams'))
    elif request.method == 'GET':
        form.games_played.data = stat1.games_played
        form.receptions.data = stat1.receptions
        form.touchdowns.data = stat1.touchdowns
        form.pass_yards.data = stat1.passing_yards
        form.completions.data = stat1.completions
        form.rush_yards.data = stat1.rushing_yards
        form.off_int.data = stat1.offensive_int
        form.def_int.data = stat1.defensive_int
        form.sacks.data = stat1.sacks
        form.tackles.data = stat1.tackles
        form.safety.data = stat1.safety
    return render_template('updateStats.html', form = form)


@app.route('/deleteTeam/<int:teamid>')
def deleteTeam(teamid):
    team = Team.query.get(teamid)
    db.session.delete(team)
    db.session.commit()
    return redirect(url_for('teams'))

@app.route('/deletePlayer/<int:playerid>')
def deletePlayer(playerid):
    player = Player.query.get(playerid)
    db.session.delete(player)
    db.session.commit()
    return redirect(url_for('teams'))


@app.route('/deleteStats/<int:playerid>')
def deleteStats(playerid):
    stats = Stats.query.filter_by(player_id = playerid).first()
    db.session.delete(stats)
    db.session.commit()
    return redirect(url_for('teams'))