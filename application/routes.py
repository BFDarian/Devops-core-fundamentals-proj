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
def teamPlayer(teamid):
    nflPlayer = Player.query.filter_by(team_id = teamid)
    return render_template('teamPlayers.html', nflPlayer = nflPlayer)


@app.route('/playerStats/<int:playerid>')
def playerStats(playerid):
    player = Player.player_name.filter_by(player_id = playerid)
    name = player.player_name
    nflPlayerStat = Stats.query.filter_by(player_id = playerid)
    return render_template('playerStats.html', nflPlayerStat = nflPlayerStat, name = name)


@app.route('/addTeam', methods=['GET','POST'])
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
        teamChoices = Team.query.filter_by(team_name = name)
        AddPlayer().team.choices.append((teamChoices.id,teamChoices.team_name))
    return render_template('addTeam.html', form = form)


@app.route('/addPlayer', methods=['GET','POST'])
def addPlayer():
    form = AddPlayer()
    if request.method == 'POST':
        name = form.player_name.data
        position = form.position.data
        height = form.height.data
        dob = form.DoB.data
        team = form.team.data
        player = Player(player_name = name, position = position, height = height, DoB = dob, team_id = team)
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('addStats', playerid = player.id ))
    return render_template('addPlayer.html', form = form)


@app.route('/addStats/<int:playerid>', methods=['GET','POST'])
def addStats(playerid):
    form = AddStats()
    if request.method =='POST':
        games = form.games_played.data
        rec = form.receptions.data
        touchdowns = form.touchdowns.data
        passY = form.pass_yards.data
        comp = form.completions.data
        rush = form.rush_yards.data
        offInt = form.off_int.data
        defInt = form.def_int.data
        sacks = form.sacks.data
        tackles = form.tackles.data
        safety = form.safety.data
        stat = Stats(games_played = games, receptions = rec, touchdowns = touchdowns, passing_yards = passY, completions = comp, rushing_yards = rush, offensive_int = offInt, defensive_int = defInt, sacks = sacks, tackles = tackles, safety = safety, player_id = playerid)
        db.session.add(stat)
        db.session.commit()
    return render_template('addStats.html', form = form)


@app.route('/updateTeam/<int:teamid>', method = ['GET', 'POST'])
def updateTeam(teamid):
    form = AddTeam()
    team = Team.query.get(teamid)
    if form.validate_on_submit:
        team.team_name = form.team_name.data
        team.team_stadium = form.stadium_name.data
        team.team_location = form.team_location.data
        team.team_owner = form.team_owner.data
        team.capacity = form.capacity.data
        db.session.commit()
        redirect(url_for('teams'))
    elif request.method == 'GET':
        form.team_name.data = team.team_name
        form.stadium_name.data = team.team_stadium
        form.team_location.data = team.team_location
        form.team_owner.data = team.team_owner
        form.capacity.data = team.capacity
    return render_template('updateTeam.html', form = form)  


@app.route('/updatePlayer/<int:playerid>', method = ['GET', 'POST'])
def updatePlayer(playerid):
    form = AddPlayer()
    player = Player.query.get(playerid)
    if form.validate_on_submit:
        player.player_name = form.player_name.data
        player.position = form.position.data
        player.height = form.height.data
        player.DoB = form.DoB.data
        player.team_id = form.team.data
        db.session.commit()
        redirect(url_for('teams'))
    elif request.method == 'GET':
        form.player_name.data = player.player_name
        form.position.data = player.position
        form.height.data = player.height
        form.DoB.data = player.DoB
        form.team.data = player.team_id
    return render_template('updatePlayer.html', form = form)


@app.route('/updateStats/<int:playerid>', methods=['GET','POST'])
def addStats(playerid):
    form = AddStats()
    stat = Stats.query.get(playerid)
    if form.validate_on_submit:
        stat.games_played = form.games_played.data
        stat.receptions = form.receptions.data
        stat.touchdowns = form.touchdowns.data
        stat.passing_yards = form.pass_yards.data
        stat.completions = form.completions.data
        stat.rushing_yards = form.rush_yards.data
        stat.offensive_int = form.off_int.data
        stat.defensive_int = form.def_int.data
        stat.sacks = form.sacks.data
        stat.tackles = form.tackles.data
        stat.safety = form.safety.data
        db.session.commit()
        redirect(url_for('teams'))
    elif request.method == 'GET':
        form.games_played.data = stat.games_played
        form.receptions.data = stat.receptions
        form.touchdowns.data = stat.touchdowns
        form.pass_yards.data = stat.passing_yards
        form.completions.data = stat.completions
        form.rush_yards.data = stat.rushing_yards
        form.off_int.data = stat.offensive_int
        form.def_int.data = stat.defensive_int
        form.sacks.data = stat.sacks
        form.tackles.data = stat.tackles
        form.safety.data = stat.safety
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
    stats = Stats.query.get(playerid)
    db.session.delete(stats)
    db.session.commit()
    return redirect(url_for('teams'))