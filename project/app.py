from flask import Flask, render_template, request, jsonify
from recipeDAO import RecipeDAO # imports the DAO

# create an instance of the DAO
recipe_dao = RecipeDAO()  

app = Flask(__name__, static_url_path='', static_folder='.') # Flask constructor
# makes static files accessible at the root URL (/) instead of /static

# Bind the index() funtion to the ‘/’ URL (homepage) 
@app.route('/')
def index():
    # Render the template 'index.html' from the 'templates' folder. render_template is good for dynamic content, so not using staticpages
    return render_template('index.html')

# curl "http://127.0.0.1:5000/recipes" 
@app.route('/recipes', methods=['GET']) # Action: Get All
def getall():
    recipes = recipe_dao.get_all()
    return jsonify(recipes)


# curl "http://127.0.0.1:5000/recipes/1"
@app.route('/recipes/<int:id>', methods=['GET']) # Action: Get. <int:id> is a variable, URL looks like ~/recipes/1
def get_recipe_by_id(id):
    recipe = recipe_dao.find_by_id(id) # uses DAO method
    return jsonify(recipe)  # Return the recipe as JSON


# curl "http://127.0.0.1:5000/recipes"
@app.route('/recipes', methods=['POST']) # Action: Create
def create_recipe():
    # read json from the body
    json_string = request.json
    return f"\ncreate {json_string}\n"


@app.route('/recipes/<int:id>', methods=['PUT']) # Action: Update
def update_recipie(id):
    json_string = request.json
    return f"\nupdate {id}{json_string}\n"


@app.route('/recipes/<int:id>', methods=['DELETE']) # Action: Delete
def delete_recipie(id):
    return "\ndelete {id}\n"


if __name__ == "__main__":
    # Start the application (in debug mode)
    app.run(debug=True)