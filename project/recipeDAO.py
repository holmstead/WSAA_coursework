import mysql.connector # for connecting python to the mysql database
from dbconfig import db_config  # import config from dbconfig.py

# create recipeDAO class
class RecipeDAO:
    # constructor
    def __init__(self):
        # connect to the database
        # **db_config unpacks the dictionary into keyword arguments
        self.db = mysql.connector.connect(**db_config) # use the config from dbconfig.py
        # creata a cursor (for executing SQL commands)
        self.cursor = self.db.cursor(dictionary=True) # return as a dictionary

    # Return all recipes
    def get_all(self):
        # execute sql query - return all rows from the recipe table
        self.cursor.execute("SELECT * FROM recipe")
        # retrieve all the results and return them
        return self.cursor.fetchall()


    # Return one recipe
    def find_by_id(self, id):
        sql = "SELECT * FROM recipe WHERE id = %s"
        self.cursor.execute(sql, (id,))
        result = self.cursor.fetchone()
        return result

    # Insert a recipe into the database
    def create(recipe):
        return recipe

    # Update a recipe
    def update(id, recipe):
        return recipe

    # Deletes a recipe
    def delete(id):
        return True
