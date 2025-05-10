# Web Services and Applications

![banner image.](img/banner.png)

This repository contains submissions for the Web Services and Applictions module at Atlantic Technologic University (ATU) 2024. 

## About

Topics include but not limited to:
-  data formats (XML, JSON, csv) and how to hanlde them
- Application Programmers Interface (APIs)
- data transfer (HTTPs, URLs, curl, POSTMAN)
- Flask (creating APIs)
- virtual environmants


## Contents


### Assignments


#### Assignment 2 - Card Draw

`assignment2-carddraw.py` simulates dealing a deck of cards. Uses Deck of Cards API https://deckofcardsapi.com


#### Assignment 3 - CSO

`assignment3-cso.py` retrieves a dataset from the Central Statistics Office (CSO).

`requests` module used - guide here: https://realpython.com/python-requests/

`json` module used - guide here:  https://www.geeksforgeeks.org/read-json-file-using-python/

- `json.dump()` used to write the contents to file


#### Assignment 4 - REST API

`assignment04-github.py`

github GET and 

- Getting started with REST api github
- https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28

- Got some fine grain tokens


### Project

A recipe database.

Started with directory structure for the project, such as putting the html page template 'index.html' in the template directory:

- https://flask.palletsprojects.com/en/stable/patterns/packages/


Created a [basic flask server](https://www.geeksforgeeks.org/flask-creating-first-simple-application/) `app.py`. Did the skeleton mapping to do some [CRUD operations.](https://www.freecodecamp.org/news/crud-operations-explained/)

Created a database using [mysql](https://www.mysql.com/) (mysql-server). MySQL is a relational database. Installed it on command line using the following command:

    $ sudo apt install mysql-server

- https://www.geeksforgeeks.org/what-is-mysql/

Launched MySQL:

    $ sudo mysql -u root -p

It ask for password. When running, created a new database using:

    create database recipe;

Insted of interactin with MySQL on the command line, I used [DBeaver](https://en.wikipedia.org/wiki/DBeaver). Created a table in the new database:

    create table recipe(
      id int NOT NULL AUTO_INCREMENT,
      PRIMARY KEY(id)
      name varchar(250)
      );

Created a new 'ingredients' column in the table:

    ALTER TABLE recipe
    ADD COLUMN ingredients TEXT;

Add another column called 'instructions':

    ALTER TABLE recipe
    ADD COLUMN instructions TEXT;     
    
seems to take ages 

-- had to stop the python app, it was connected to database and preventing the update column operation. Found that ouy by reading the output from the following:

    SHOW PROCESSLIST;

Created a [Database Access Object (DAO)](https://www.geeksforgeeks.org/data-access-object-pattern/) `recipeDAO.py`.

I put the database config info into a seperate file `dbconfig.py`.

In the DAO "mysql.connector" is used for connecting python to the mysql database - [W3 schools](https://www.w3schools.com/python/python_mysql_getstarted.asp)

Imported the DAO into the server `app.py`.

    from DAO import recipeDAO

Called the DAO methods (get_all, find_by_id) from the app, and returned using [jsonify](https://pytutorial.com/flask-jsonify-create-json-responses-in-flask-applications/).

Created html - stored in /templates directory. It houses the javascript and ajax functions (client side). Ajax functions take the https requests. Javascript deals with the functionality i.e. what happens when you click a button.

AJAX (Asynchronous JavaScript and XML) is a method where you use JavaScript to send or receive data from a server without refreshing the page.

The html is the static part of the user interface.

    javascript function > ajax function > server > DOA > SQL database

This bit hides the form for editing recipe, until the button is clicked:

    function editRecipe(id) {
        document.getElementById(`view-${id}`).style.display = 'none';
        document.getElementById(`edit-${id}`).style.display = 'block';
    }

`style.display = 'none'` This makes the element invisible and removes it from the layout (it doesn’t take up space in the document).

`style.display = 'block'` This makes the element visible and displays it as a block-level element, which means it will appear on the page normally.

 The button for which is at the beginning of the html file

    <button onclick="updateRecipe(${recipe.id})">Save</button>

Added a cancel button for when editing a recipe, in case you dont want to save any changes

    <button onclick="cancelEdit(${recipe.id})">Cancel</button>


Seperated webppage style into css file. Lots of css templates [here](https://www.w3schools.com/w3css/w3css_templates.asp).


For the button containers I used [flexbox](https://www.w3schools.com/csS/css3_flexbox.asp) in the css:

    /* Center buttons inside the button-container */
    .button-container {
        display: flex;             /* Use flexbox */
        justify-content: center;   /* Center buttons horizontally */
        gap: 10px;                 /* Space between buttons */
        margin-top: 10px;          /* Optional: add some space above the buttons */
    }

Hosted on [pythonanywhere](https://www.pythonanywhere.com/). First I made a github repo to deploy from:

- [holmstead/deploytopythonanywhere](https://github.com/holmstead/deploytopythonanywhere)

Cloned repo to local machine:

    git clone git@github.com:holmstead/deploytopythonanywhere.git

Created new basic server `flask_app.py` to test out the setup on pythonanywhere.

Set up a [virtual env](https://docs.python.org/3/library/venv.html):

    python -m venv venv

Activated the environment (from parent directory):
    
    source venv/bin/activate

Tested if server worked:

    python3 flask_app.py

Had to pip install `mysql-connector` in the virtual environment. Pushed up to github. Then went to pythonanywhere website and started a new bash console and cloned the repo:

    git clone https://github.com/holmstead/deploytopythonanywhere.git   (https)

Go to 'Open Web tab' and selected 'new web app'. Set the soiurce code as follows:

    Source code: /home/holmstead/deploytopythonanywhere

Created requirements file:

    pip freeze requirements.txt

Created new database "recipes".

Checked if that worked:

    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | holmstead$default  |
    | holmstead$recipes  |
    | information_schema |
    | performance_schema |
    +--------------------+

Selected the new database

    mysql> use holmstead$recipes

Its empty, so then set up tables like the local database 'recipes'

    CREATE TABLE recipe (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(250),
        ingredients TEXT,
        instructions TEXT,
        PRIMARY KEY (id)
    );

Then checked if it worked:

    mysql> show tables;
    +-----------------------------+
    | Tables_in_holmstead$recipes |
    +-----------------------------+
    | recipe                      |
    +-----------------------------+


Then went to bash console:

    cd deploytopythonanywhere

    git pull


Set up dbconfig.py to have the pythonanywhere database details:

    db_config = {
        "host": "holmstead.mysql.pythonanywhere-services.com",
        "user": "holmstead",
        "password": "neoMorpheus",
        "database": "holmstead$recipes"
    }

And it worked, link to hosted web app:

- https://holmstead.pythonanywhere.com/

## Get Started

Clone the repository:

```
$ git clone https://github.com/holmstead/WSAA_coursework.git
```

### Requirements

1. **Python**: Version 3.7 or higher. You can download it from [python.org](https://www.python.org/downloads/).

2. **Dependencies**: Install the required Python packages by running:
  ```bash
  $ python pip install -r requirements.txt
   ```


## Get Help

VSCode help can be found using the links below:

- https://code.visualstudio.com/docs/introvideos/basics

Requests module:

- https://docs.python-requests.org/en/latest/index.html


## Author

M. Holmes, 2024

holmstead@protonmail.com

## References

Flask user guide:

- https://flask.palletsprojects.com/en/stable/

Flask tutorial:

- https://www.geeksforgeeks.org/flask-tutorial/

The [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) in the offical docs.


[freeCodeCamp flask tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on youtube:

