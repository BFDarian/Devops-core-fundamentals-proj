from flask_testing import LiveServerTestCase
from selenium import webdriver
from urllib.request import urlopen
from flask import url_for

from application import app, db
from application.models import Team, Player
from datetime import datetime

class TestBase(LiveServerTestCase):
    TEST_PORT = 5050 # test port, doesn't need to be open

    def create_app(self):

        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///testTeam.db",
            LIVESERVER_PORT=self.TEST_PORT,
            
            DEBUG=True,
            TESTING=True
        )

        return app

    def setUp(self):

        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument('--headless')

        self.driver = webdriver.Chrome(options=chrome_options)

        db.create_all()

        team = Team(team_name = '49ers', 
                    team_stadium = 'test stadium', 
                    team_location = 'SF', 
                    team_owner = 'John Smith', 
                    capacity = 70000)

        player = Player(player_name = 'Donald', 
                    position = 'DL', 
                    height = 190, 
                    DoB = datetime(1995,11,11,10,10,10), 
                    team_id = 1)

        db.session.add(team)
        db.session.add(player)
        db.session.commit()

        self.driver.get(f'http://localhost:{self.TEST_PORT}')

    def tearDown(self):
        self.driver.quit()

        db.drop_all()

    def test_server_is_up_and_running(self):
        response = urlopen(f'http://localhost:{self.TEST_PORT}')
        self.assertEqual(response.code, 200)

class TestAddTeam(TestBase):
    name = 'Rams'
    loc = 'LA'

    def submit_input(self): # custom method
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="team_name"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="team_location"]').send_keys(self.loc)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        text = self.driver.find_element_by_xpath('/html/body/a[5]').text
        self.assertIn('Rams', text )

    def test_empty_validation(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.assertIn(url_for('addTeam'), self.driver.current_url)

        teams = Team.query.all()
        self.assertEqual(len(teams), 1) 

class TestAddPlayer(TestBase):
    name = 'Ramsey'
    team = 'LA Rams'

    def submit_input(self): # custom method
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="player_name"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="team"]').send_keys(self.team)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        player = Player.query.filter_by(player_name = self.name).first()
        self.assertIn('Ramsey', player.player_name)

    def test_empty_validation(self):
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.assertIn(url_for('addPlayer'), self.driver.current_url)

        players = Player.query.all()
        self.assertEqual(len(players), 1)


class TestUpdateTeam(TestBase):

    name = '49ers1'
    loc = 'San Diego'

    def submit_input(self): # custom method
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('/html/body/a[10]').click()
        self.driver.find_element_by_xpath('//*[@id="team_name"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="team_location"]').send_keys(self.loc)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        text = self.driver.find_element_by_xpath('/html/body/a[5]').text
        self.assertIn('49ers1', text )

class TestUpdatePlayer(TestBase):

    name = 'Donald1'

    def submit_input(self): # custom method
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('/html/body/a[5]').click()
        self.driver.find_element_by_xpath('/html/body/a[9]').click()
        self.driver.find_element_by_xpath('//*[@id="player_name"]').send_keys(self.name)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/a[5]').click()
        text = self.driver.find_element_by_xpath('/html/body/a[5]').text
        self.assertIn(self.name, text )