import mysql.connector # for connecting python to the mysql database

# create recipeDAO class
class RecipeDAO:
    # constructor
    def __init__(self):
        # connect to the database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="recipes"
        )
        # creata a cursor (for executing SQL commands)
        self.cursor = self.db.cursor(dictionary=True) # return as a dictionary

    def get_all(self):
        # execute sql query - return all rows from the recipe table
        self.cursor.execute("SELECT * FROM recipe")
        # retrieve all the results and return them
        return self.cursor.fetchall()



# Return one recipe
def findById(id):
    return {}

# Insert a recipe into the database
def create(recipe):
    return recipe

# Update a recipe
def update(id, recipe):
    return recipe

# Deletes a recipe
def delete(id):
    return True
