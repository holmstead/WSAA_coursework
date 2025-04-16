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

- #### Assignment 2 - Card Draw

assignment2-carddraw.py - simulates dealing a deck of cards. Uses Deck of Cards API https://deckofcardsapi.com

#### Assignment 3 - CSO

**assignment3-cso.py** - retrieves a dataset from the Central Statistics Office (CSO).

`requests` module used - guide here: https://realpython.com/python-requests/

`json` module used - guide here:  https://www.geeksforgeeks.org/read-json-file-using-python/

- json.dump() used to write the contents to file

#### Assignment 4 - REST API

**assignment04-github.py**

github GET and 

- Getting started with REST api github
- https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28

- Got some fine grain tokens


### Project

A recipe database.

Flask user guide:

- https://flask.palletsprojects.com/en/stable/

Stuff like render_template() and that covered here:

- https://flask.palletsprojects.com/en/stable/api/

Flask tutorial:

- https://www.geeksforgeeks.org/flask-tutorial/

The [Flask tutorial](https://flask.palletsprojects.com/en/stable/tutorial/) in the offical docs wasa a lot of help, especially the [application setup](https://flask.palletsprojects.com/en/stable/tutorial/factory/) bit when starting the project.


[freeCodeCamp flask tutorial](https://www.youtube.com/watch?v=Z1RJmh_OqeA) on youtube:


Started with directory structure for the project, such as putting the html page template 'index.html' in the template directory:

- https://flask.palletsprojects.com/en/stable/patterns/packages/


Created a basic flask server "app.py". Did the skeleton mapping to do some CRUD operations.


Created a database using [mysql](https://www.mysql.com/) (mysql-server). Installed on command line:

  - $ sudo apt install mysql-server

Launched my sql:

  $ sudo mysql -u root

When running, created a new database using:

  - create database recipes;

Then created a table in the new database:

  - create table recipe(
      id int NOT NULL AUTO_INCREMENT,
      PRIMARY KEY(id)
      name varchar(250)
      );

Created a new column in the table:

  ALTER TABLE recipe
  ADD COLUMN ingredients TEXT;

Created a [Database Access Object (DAO)](https://www.geeksforgeeks.org/data-access-object-pattern/) "recipeDAO.py".

I put the database config info into a seperate file "dbconfig.py".

In the DAO "mysql.connector" is used for connecting python to the mysql database - [W3 schools](https://www.w3schools.com/python/python_mysql_getstarted.asp)

Imported the DAO into the server "app.py."

  from DAO import recipeDAO # imports the DAO


Called the DAO methods (ge_all, find_by_id) from the app, and returned using [jsonify](https://pytutorial.com/flask-jsonify-create-json-responses-in-flask-applications/).


Got a [basic html template](https://www.freecodecamp.org/news/basic-html5-template-boilerplate-code-example/).

Created html file for each page:
  - recipes.html for get_all()
  - recipe.html for get_recipe_by_id()

  stored them in /templates directory



Seperated webppage style into css file
Lots of css templates here:

  https://www.w3schools.com/w3css/w3css_templates.asp


Host on [pythonanywhere](https://www.pythonanywhere.com/).



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

