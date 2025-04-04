import mysql.connector # for connecting python to the mysql database

# Create a connection to the MySQL server.
connection = mysql.connector.connect(
    #TODO put in config file
    host="localhost",
    user="root",
    password="root"
    )

# Create a cursor to execute queries
mycursor = connection.cursor()

# example query
sql= "SHOW DATABASES"

# Execute sql queyr
mycursor.execute(sql)


# Return all recipes in the database table
def getall():
    return [{}]

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



# Close the cursor and connection
mycursor.close()
connection.close()