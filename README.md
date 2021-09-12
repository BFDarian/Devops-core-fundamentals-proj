# Devops-core-fundamentals-proj


# Contents
* Brief
* Architecture
* Project Tracking
* Risk Assessment
* Testing
* Front-End App
* Known Issues
* Future Improvements



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