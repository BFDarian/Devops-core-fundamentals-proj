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


## Project Tracking



Link to trello: https://trello.com/b/lNu17dLf/devops-project-nfl-app


![Trello](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/Trello.png)

Trello was used to track the progress of the project and break down the project to it's fundamentals.

The board starts with the backlog where users stories and app functionality would be outlined and broken up in to notes. The plannin stage was for notes taht were bneing prepared but were not quite ready for implementaiton duew to either another are of functionality was required first or more research in how to implement the note was required.


For version control, git was used and the project repo was on GitHub. Version control allows for the project to be modified and commited while also having access to earlier version of the project if an error in the latest commit causes the project to break. This means the project can be reverted to the last working commit if needed and provides a safe place to rometly store a project incase issues on a local machince causes developers to lose their files. 

For the development of  the project python was used with a virtual environment(venv) hosted on a aws virtual machine runnig Ubuntu. Flask was used to design the webpages and MySQL was used for the database. Jenkins is used to provide automation to testing and building of the project. It will pull the latest commit from the GitHub repo and run tests on the code and then build up the app to view. 




## Risk Assessment

![Risk Assessment](https://github.com/BFDarian/Devops-core-fundamentals-proj/blob/dev/design/Trello.png)