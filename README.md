# Devops-core-fundamentals-proj


# Contents
* [brief](#brief)
* [Architecture](#architecture)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Testing](#testing)
* [Front-End App](#front-end-app)
* [Known Issues](#known-issues)
* [Future Improvements](#future-improvements)




## Brief:

The brief provided for this project was to design a webpage application which utilised CRUD (create, read, update and delete) functionality, so we could store information in a MySQL database. We would also have to make use of the python framework Flask and other extensions to help design the database, webpages and forms. 


For this project we also had other requirements set out inthe brief. These consist of a Trello board, to organise our user stories and create sprints, a standalone relational database containing a minimum of two tables which must be normalised to avoid many-to-many relationships between tables, test cases created and run using pytest and version control.

### My approach

To achieve the brief i have chosen to build an NFL statistics app, which allows users to create teams and add players their statistics to a team(create). The users can then view all teams in the database and select which one they would like to view which takes you to view all the player taht play for that team and each players individual stats(read). Furthermore, each aspect of app (the teams, players and players stats) can all be updated to maintain the reliabilty of the app.


## Architecture

The database for this project consists of three tables:
- Teams
- Players
- Stats

The relationships between these tables are as follows:
- Teams to Player - One team can have many players but one player may only have one team
- Player to Stats - One player has one set of stats and one set of stats belongs to one player

![ERD](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/NFL_ERD.png)


## Project Tracking



Link to trello: https://trello.com/b/lNu17dLf/devops-project-nfl-app


![Trello](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/Trello.png)

Trello was used to track the progress of the project and break down the project to it's fundamentals.

The board starts with the backlog where users stories and app functionality would be outlined and broken up in to notes. The planning stage was for notes that were being prepared but were not quite ready for implementation due to either more functionality was required first or further research in how to implement the note was required.


For version control, git was used and the project repo was on GitHub. Version control allows for the project to be modified and commited while also having access to earlier version of the project if an error in the latest commit causes the project to break. This means the project can be reverted to the last working commit if needed and provides a safe place to rometly store a project incase issues on a local machince causes developers to lose their files. 

For the development of  the project python was used with a virtual environment(venv) hosted on a aws virtual machine runnig Ubuntu. Flask was used to design the webpages and MySQL was used for the database. Jenkins is used to provide automation to testing and building of the project. It will pull the latest commit from the GitHub repo and run tests on the code and then build up the app to view. 

![pipeline](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/pipeline.png)



## Risk Assessment

![Risk Assessment](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/Risk_assessment.png)

Most of the risk were identified beforehand except for one. This was where my instance kept crashing in the middle of testing. This caused me to lose some code due to not having pushed to my repo. This meant I had to  try reload the instance just so I could quickly push what I had saved to github in hopes to save some of my progress. Thankfully I managed to and then set up a new instance as I did not wish to risk losing any further progress.


## Testing

For testing the application we used pytest. There are two types of test ran on the app, unit tests and integration tests. Unit tests test the functionality of the functions withing the app. In this project that is the CRUD functionality, so each test is written to test individual segments of CRUD. Integration testing tests the app in a live environment to ensure the app acts as intended by mimicing keyboard andf dmouse inputs.

![coverage test](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/CoverageReport.png)


## Front-End App

### home page


![Home page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/home.png)

From the home page the user is given links to direct to any of the other main pages.

![Add Team page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/newTeam.png)

Next is the add teams page where the user is prompted to input data about the team.

![View Team page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/viewTeam.png)

Upon submitting a new team the user gets redirected to the view teams page where thy can see all teams that have already been made. From here you can update/delte a team or view the players of that team.


![Add Player page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/newPlay.png)

Here the user can add a player to the database. Afterwards you get redirected to the add stats page for that player.


![Add Player Stats page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/AddPlayerStat.png)

Here the user add the stats for the player they just added to the database.

![View Player page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/viewPlayer.png)

From the view teams page the user can select the team they want and view all the players in that team who will be displayed on a new page. From here you can also update the player information or delete the player

![View Player Stats page](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/ViewStats.png)

From the view player page you can select any player on that page and view theri stats. From here you can update the player information. You cannot delte as I came the the realisation that you can't add a player without adding stats for the player so i thought it would be best if to make it sothe user cannot delete stats for a player without deleting the player as well.

There are also update pages for Teams, Players and Stats but they are identical to the add pages just with a different title and the information already know abouth te player is automatically filled in.


## Known Issues

- There is no prevention to stop the user andding the same team or player multiple times.

## Future Improvements

- I would like to add more tables for players so taht I can seperate player by position so I can therefore tailor the stats shown for the player.

- Add a user login so users can personalise their own app and just have teams and players they want.

- Fix the issue stated above so that teams and players only appear once. 