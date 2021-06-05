# BLITZ

----------------------------------------------

## Description
Blitz is an application that allows to manage chess tournaments.

## Installation

* The application was developed with Python 3.9.2
* The following installation procedure applies to a Windows environment using Cmder(bash).

### clone repository

```bash
$ git clone https://github.com/dardevetdidier/blitz.git 
```

### create and activate virtual environment

```bash
$ cd /project_directory
$ python -m venv venv
$ source venv/Scripts/activate
```

### Install Python packages

```bash
$ pip install -r requirements.txt
```

### Execute the script

```bash
$ cd /project_directory
$ python blitz.py
```

## Usage

Although it is an application running in a terminal, the menus allow good ergonomics and guide the user easily.
For a better experience by improving display, run Blitz with terminal in full-screen mode.

* When you start application there are no tournaments running. You have to load a tournament or create a new one in
  Tournament Menu. After you've loaded a tournament you can create a new round. 
* Create a new tournament. You can choose to add a player saved in database or to add him manually.(If players' database
  is empty you have to add players manually).
  The program automaticaly saves information of the players and saves the tournament.
* Create a new round. 
  * A tournament consists of 4 rounds. 
  * The program creates pairs according to the Swiss system. 
* Enters the results of each match : 
  * win = 1 ; lose = 0 ; draw = 0.5 for each player.
  * The program finishes the round and purpose you to create another one to continue the tournament. 
  * Results are automaticaly saved and players' ranking are updated.
* In Players Menu, you can manually modify a player's ranking by choosing him from a list. The programm saves new
ranking.
* Several tournaments can be saved. You don't have to finish one tournament to continue another. You've just to 
  interrupt a tournament (3rd option in Main Menu) and creates a new one or load an existing tournament (2nd option
  in Main Menu)
* The Reports Menu allows you to display information about tournaments, rounds, matches and players.
  You just have to choose in the menu what you want to be displayed.
* To exit the app choose '5' in Main Menu.  
  
## Generate a new flake8 html report

*flake8 and flake8-html packages are in requirements.txt. To generate the flake8 report you have to first 
activate Virtual environment (see above)*

```bash
$ cd /project_directory
$ flake8 -v --max-line-length=119 --format=html --htmldir=flake8_rapport blitz.py ./models ./controllers ./views
```

It creates a 'flake-report' folder in project directory. You can open the 'index.html' file in a web browser to show 
the report results. 
   
  