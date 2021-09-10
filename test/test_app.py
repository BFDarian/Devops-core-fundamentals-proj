from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import Team, Player, Stats
from datetime import datetime

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///testTeam.db",
                SECRET_KEY = 'TEST_SECRET_KEY',
                DEBUG = True,
                WTF_CSRF_ENABLED = False)
        return app
    
    def setUp(self):
        db.create_all()
        sampleT = Team(team_name = 'testing', 
                    team_stadium = 'test stadium', 
                    team_location = 'test city', 
                    team_owner = 'John Smith', 
                    capacity = 50000)
        
        sampleP = Player(player_name = 'tester', 
                        position = 'QB', 
                        height = 190, 
                        DoB = datetime(1995,11,11,10,10,10), 
                        team_id = 1)
        
        sampleS = Stats(games_played = 239, 
                        receptions = 0, 
                        touchdowns = 270, 
                        passing_yards = 17000, 
                        completions = 4000, 
                        rushing_yards = 400, 
                        offensive_int = 100,
                        defensive_int = 0, 
                        sacks = 0, 
                        tackles = 0, 
                        safety = 0, 
                        player_id = 1)
        db.session.add(sampleT)
        db.session.add(sampleP)
        db.session.add(sampleS)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

class TestHome(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'NFL app', response.data)

class TestTeamGet(TestBase):
    def test_teams(self):
        response = self.client.get(url_for('teams'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Teams', response.data)

class TestPlayerGet(TestBase):
    def test_teamPlayers(self):
        response = self.client.get(url_for('teamPlayers', teamid = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Players', response.data)

class TestPlayerStatGet(TestBase):
    def test_playerStats(self):
        response = self.client.get(url_for('playerStats', playerid = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Stats', response.data)

class TestAddTeamGet(TestBase):
    def test_addTeam(self):
        response = self.client.get(url_for('addTeam'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add a New Team', response.data)

class TestAddTeamPost(TestBase):
    def test_addTeam(self):
        response = self.client.post('/addTeam', 
                    data = dict(team_name = 'Test1' , 
                                team_stadium = 'Test1 Stadium', 
                                team_location = 'Test1 city', 
                                team_owner = 'Jane Doe', 
                                capacity= 20000),
                                follow_redirects = True)
        self.assertIn(b'Teams', response.data)

class TestAddPlayerGet(TestBase):
    def test_addPlayer(self):
        response = self.client.get(url_for('addPlayer'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add a New Player', response.data)

class TestAddPlayerPost(TestBase):
    def test_addPlayer(self):
        response = self.client.post(url_for('addPlayer'), 
                    data = dict(player_name = 'tester1', 
                                position = 'RB', 
                                height = 178, 
                                DoB = datetime(1996,10,9,10,10,10), 
                                team_id = 2),
                                follow_redirects = True)
        self.assertIn(b'Add Player Stats', response.data)

class TestAddStatsGet(TestBase):
    def test_addStats(self):
        response = self.client.get(url_for('addStats', playerid = 2))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Add Player Stats', response.data)

class TestAddStatsPost(TestBase):
    def test_addStats(self):
        response = self.client.post(url_for('addStats', playerid = 2), 
                    data = dict(games_played = 140 , 
                                receptions = 200, 
                                touchdowns = 220, 
                                passing_yards = 500, 
                                completions = 0, 
                                rushing_yards = 13000, 
                                offensive_int = 0,
                                defensive_int = 0, 
                                sacks = 0, 
                                tackles = 0, 
                                safety = 0, 
                                player_id = 2),
                                follow_redirects = True)
        self.assertIn(b'Teams', response.data)
    

class TestUpdateTeamGet(TestBase):
    def test_updateTeam(self):
        response = self.client.get(url_for('updateTeam', teamid = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Team', response.data)

class TestUpdateTeamPost(TestBase):
    def test_updateTeam(self):
        response = self.client.post(url_for('updateTeam', teamid = 1), 
                    data = dict(team_name = 'UpdateTest1' , 
                                team_stadium = 'UpdateTest1 Stadium', 
                                team_location = 'UpdateTest1 city', 
                                team_owner = 'UpdateJane Doe', 
                                capacity= 25000),
                                follow_redirects = True)
        self.assertIn(b'Teams', response.data)

class TestUpdatePlayerGet(TestBase):
    def test_updatePlayer(self):
        response = self.client.get(url_for('updatePlayer', playerid = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Player', response.data)

class TestUpdatePlayerPost(TestBase):
    def test_updatePlayer(self):
        response = self.client.post(url_for('updatePlayer', playerid = 1), 
                    data = dict(player_name = 'Updatetester1', 
                                position = 'WR', 
                                height = 175, 
                                DoB = datetime(1999,6,11,10,10,10), 
                                team_id = 1),
                                follow_redirects = True)
        self.assertIn(b'Teams', response.data)

class TestUpdateStatsGet(TestBase):
    def test_updateStats(self):
        response = self.client.get(url_for('updateStats', playerid = 1))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Update Stats', response.data)

class TestUpdateStatsPost(TestBase):
    def test_UpdateStats(self):
        response = self.client.post(url_for('updateStats', playerid = 1), 
                    data = dict(games_played = 130 , 
                                receptions = 600, 
                                touchdowns = 100, 
                                passing_yards = 7500, 
                                completions = 0, 
                                rushing_yards = 0, 
                                offensive_int = 0,
                                defensive_int = 0, 
                                sacks = 0, 
                                tackles = 0, 
                                safety = 0),
                                follow_redirects = True)
        self.assertIn(b'Teams', response.data)

class TestDelTeam(TestBase):
    def test_DelTeam(self):
        response = self.client.get(url_for('deleteTeam', teamid = 1), follow_redirects = True)
        self.assertNotIn(b'testing', response.data)

class TestDelPlayer(TestBase):
    def test_DelPlayer(self):
        response = self.client.get(url_for('deletePlayer', playerid = 1), follow_redirects = False)
        self.assertNotIn(b'tester', response.data)