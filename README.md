# Web Services and Applications

![banner image.](img/banner.png)

This repository contains submissions for the Web Services and Applictions module at Atlantic Technologic University (ATU) 2024. 

## About

Topics include but not limited to:
- data formats (XML, JSON, csv) and how to hanlde them
- Application Programmers Interface (APIs)
- data transfer (HTTPs, URLs, curl, POSTMAN)
- Flask (python library for creating APIs)
- virtual environments


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

GitHub GET and 

- Getting started with REST API GitHub
- https://docs.github.com/en/rest/using-the-rest-api/getting-started-with-the-rest-api?apiVersion=2022-11-28

- Got some fine grain tokens


### Project - A recipe database.

The project directory structure was modelled on Flasks [package pattern](https://flask.palletsprojects.com/en/stable/patterns/packages/) guide.

A database was created locally using [MySQL](https://www.mysql.com/) (mysql-server). MySQL is a [relational database](https://www.oracle.com/database/what-is-a-relational-database/). Install mysql using the following command:

    sudo apt install mysql-server

- https://www.geeksforgeeks.org/what-is-mysql/

Launched MySQL:

    sudo mysql -u root -p

Created a new database called 'recipe':

    CREATE DATABASE recipe;

Instead of interacting with MySQL on the command line, I used [DBeaver](https://en.wikipedia.org/wiki/DBeaver). Created a table in the new database:

    CREATE TABLE recipe (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(250),
        ingredients TEXT,
        instructions TEXT,
        PRIMARY KEY (id)
    );


Created a [Database Access Object (DAO)](https://www.geeksforgeeks.org/data-access-object-pattern/) `recipeDAO.py`. The RecipeDAO is a [class](https://docs.python.org/3/tutorial/classes.html) that handles the database operations - [CRUD operations](https://www.freecodecamp.org/news/crud-operations-explained/):

- Create: Adding new recipes to the database
- Read: Retrieving recipes
- Update: Modifying existing recipe details
- Delete: Removing recipes from the database

The database connection info is stored in a seperate file `dbconfig.py`. This improves security and modularity. `mysql.connector` is used for [connecting to the mysql database](https://www.w3schools.com/python/python_mysql_getstarted.asp).

The DAO class is imported into the server app.py, which functions as a [RESTful API](https://www.geeksforgeeks.org/what-is-restful-api/). It handles HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE` to perform operations on the database. The [mapping](https://www.geeksforgeeks.org/flask-app-routing/) between these HTTP methods and specific URL routes is defined using Flask’s `@app.route()` decorator. 

The app calls DAO methods like `get_all` and `find_by_id`, then uses [jsonify](https://pytutorial.com/flask-jsonify-create-json-responses-in-flask-applications/) to convert the returned data into JSON format .

Stored in the `/templates` directory is static HTML for the front-end. It houses the [Javascript](https://www.w3schools.com/whatis/whatis_js.asp) code and uses [AJAX](https://www.w3schools.com/xml/ajax_intro.asp) (Asynchronous JavaScript and XML) methods on the client side.

AJAX functions handle the HTTP requests (such as GET, POST, PUT, DELETE), while JavaScript is responsible for the overall functionality — such as what happens when you click a button or interact with other elements on the page. 

Some good examples of AJAX methods can be found on [W3 Schools AJAX](https://www.w3schools.com/js/js_ajax_examples.asp) examples.

[Javascript functions](https://www.w3schools.com/js/js_functions.asp):

- `submitNewRecipe()` sends a new recipe to the server.  Reads values from the "Add Recipe" form. Sends a POST request to /add_recipe with the recipe details in JSON. Reloads the page after submission to show the updated list.

- `deleteRecipe(id)`
Deletes a recipe from the database. Asks the user for confirmation using confirm(). If confirmed, sends a DELETE request to /recipes/{id}. Reloads the page afterward to reflect the change.

- `editRecipe(id)` Opens the "Edit Recipe" form pre-filled with the selected recipe's data. Gets the recipe’s current data (name, ingredients, instructions) from the displayed HTML. Fills in the hidden edit form with those values. Hides the current recipe display and shows the edit form.

 - `updateRecipe()` Sends updated recipe information to the server. Reads values from the "Edit Recipe" form. Sends a PUT request to /recipes/{id} with updated data. Reloads the page to reflect the changes.

- `closeEditForm()` Closes the edit form without saving changes. Hides the edit form. Redisplays the original recipe block.

- `closeAddForm()` Hides the "Add New Recipe" form when the user cancels. Sets the form's display style to none

- `window.addEventListner` Used instead of the older way of using `window.onload` (seen [here](https://stackoverflow.com/questions/20180251/when-to-use-window-onload.)).  This sends a GET request to fetch all the recipes from the Flask backend. It generates some dynamic html to display each recipe, and creates edit/delete buttons for each recipe. 

To add a new recipe there is a button that will bring up the (hidden) form [on click](https://www.w3schools.com/jsref/event_onclick.asp) to type the recipe info into:

    <button onclick="updateRecipe(${recipe.id})">Save</button>

The 'update recipe' and 'add new recipe' [forms are hidden](https://bobbyhadz.com/blog/javascript-hide-element-by-id) until the relevent button is clicked:

    function editRecipe(id) {
        document.getElementById(`view-${id}`).style.display = 'none';
        document.getElementById(`edit-${id}`).style.display = 'block';
    }

`style.display = 'none'` This makes the element invisible and removes it from the layout (it doesn’t take up space in the document).

`style.display = 'block'` This makes the element visible and displays it as a block-level element, which means it will appear on the page normally.


Theres also a cancel button available when adding/editing a recipe, in case you don't want to save any changes. The function:

    // Close Add Form
    function closeAddForm() {
        document.getElementById('addRecipeForm').style.display = 'none';
    }

... basically hides the form again when the button is pressed:

    <button type="button" onclick="closeAddForm()">Cancel</button>

The delete button when pressed will [prompt for confirmation](https://www.codexworld.com/how-to/show-delete-confirmation-message-dialog-javascript/):

    // Show confirmation dialog
    const isConfirmed = confirm("Are you sure you want to delete this recipe?");

Values are read from form elements in the [DOM](https://www.w3schools.com/js/js_htmldom.asp) using the getElementById() function:

    const name = document.getElementById('newName').value;

The [`fetch()`](https://www.geeksforgeeks.org/javascript-fetch-method/) function can be used to send HTTP requests with different methods such as POST, PUT, DELETE, and GET, in JSON format:

    fetch('/add_recipe', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name, ingredients, instructions })
    })


#### CSS

The webppage styling is seperated into a [CSS](https://www.w3schools.com/Css/css_intro.asp) file, []'external CSS'](https://www.w3schools.com/CSS/css_howto.asp). Lots of CSS templates can be found [here](https://www.w3schools.com/w3css/w3css_templates.asp).

[HTML is linked to the CSS](https://www.geeksforgeeks.org/how-to-link-a-css-file-to-html/) so that styles defined in the CSS file can be applied to elements in the HTML page:

    <link rel="stylesheet" href="styles.css">

The [card](https://www.w3schools.com/howto/howto_css_cards.asp) class is used to group the content in a nice way on the page.

For the body and button containers I used [flexbox](https://www.w3schools.com/csS/css3_flexbox.asp) which dynamically adjusts the content layout in the container:

    /* Body */
    body {
        font-family: 'Segoe UI', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 100vh; /* Full viewport height */
        margin: 0;
        padding: 0;
        background-color: #f0f0f0;
        color: #333;
        line-height: 1.6;
    }

#### Hosting on [pythonanywhere](https://www.pythonanywhere.com/)

First, made a github repo to deploy from:

- [holmstead/deploytopythonanywhere](https://github.com/holmstead/deploytopythonanywhere)

Cloned repo to local machine:

    git clone git@github.com:holmstead/deploytopythonanywhere.git

Set up a [virtual env](https://docs.python.org/3/library/venv.html) on local machine:

    python -m venv venv

Activated the environment (from parent directory):
    
    source venv/bin/activate

Copied all the server files to the directory and tested if server worked:

    python3 flask_app.py

Had to pip install `mysql-connector` in the virtual environment. Pushed up to github. Created requirements file:

    pip freeze requirements.txt
    
Started a new bash console on pythonanywhere and cloned the repo:

    git clone https://github.com/holmstead/deploytopythonanywhere.git   (https)

Created new database "recipes". Checked if it worked:

    mysql> show databases;
    +--------------------+
    | Database           |
    +--------------------+
    | holmstead$default  |
    | holmstead$recipes  |
    | information_schema |
    | performance_schema |
    +--------------------+

Selected the new database:

    mysql> use holmstead$recipes

The new database is empty, so tables were set up like the local database 'recipe':

    CREATE TABLE recipe (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(250),
        ingredients TEXT,
        instructions TEXT,
        PRIMARY KEY (id)
    );

Check if new table was created:

    mysql> show tables;
    +-----------------------------+
    | Tables_in_holmstead$recipes |
    +-----------------------------+
    | recipe                      |
    +-----------------------------+


Then go to bash console:

    cd deploytopythonanywhere

    git pull


Set up dbconfig.py to have the pythonanywhere database details:

    db_config = {
        "host": "holmstead.mysql.pythonanywhere-services.com",
        "user": "holmstead",
        "password": "neoMorpheus",
        "database": "holmstead$recipes"
    }

And it worked! Link to hosted web app:
- https://holmstead.pythonanywhere.com/


## Get Started

Clone the repository:


    git clone https://github.com/holmstead/WSAA_coursework.git


### Requirements

1. **Python**: Version 3.7 or higher. You can download it from [python.org](https://www.python.org/downloads/).

2. **Dependencies**: Install the required Python packages:

        python pip install -r requirements.txt

3. **MySQL**: Install the relational database: 

        sudo apt install mysql-server

## Author

M. Holmes, 2025

holmstead@protonmail.com

## References

Flasks official user guide:
- https://flask.palletsprojects.com/en/stable/

Flask tutorial on geeksforgeeks website:
- https://www.geeksforgeeks.org/flask-tutorial/

The Flask tutorial in the offical docs:
- https://flask.palletsprojects.com/en/stable/tutorial/

Flask tutorial by freeCodeCamp:
- https://www.youtube.com/watch?v=Z1RJmh_OqeA

Creating a basic flask server:
- https://www.geeksforgeeks.org/flask-creating-first-simple-application/

Flask server example with AJAX methods:
- https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688/

Real Python covers frontend (HTML, Javascript, CSS) in this project:
- https://realpython.com/flask-javascript-frontend-for-rest-api/

Banner image generated using [DALL.E 3](https://openai.com/index/dall-e-3/) by OpenAI.

Code debugging and refactoring was done with the aid of a locally-installed open-source Large Language Model (LLM) [Ollama](https://github.com/ollama/ollama), specifically the Code LLama model.
