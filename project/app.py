from flask import Flask, render_template, request, jsonify
from recipeDAO import RecipeDAO # imports the DAO

# create an instance of the DAO
recipe_dao = RecipeDAO()  

app = Flask(__name__, static_url_path='', static_folder='.') # Flask constructor
# makes static files accessible at the root URL (/) instead of /static

# Bind the index() funtion to the ‘/’ URL (homepage) 
@app.route('/')
def index():
    # Render the template 'index.html' from the 'templates' folder
    return render_template('index.html')

# curl "http://127.0.0.1:5000/recipes" 
@app.route('/recipes', methods=['GET']) # Action: Get
def getall():
    # Fetch all recipes from the DAO
    recipes = recipe_dao.get_all()
    # Render the recipes template with the recipes data
    return render_template('recipes.html', recipes=recipes)


# curl "http://127.0.0.1:5000/recipes/1"
@app.route('/recipes/<int:id>', methods=['GET']) # Action: Get. <int:id> is a variable, URL looks like ~/recipes/1
def get_recipe_by_id(id):
    recipe = recipe_dao.find_by_id(id)
    if recipe:
        return jsonify(recipe)  # Return recipe as JSON
    else:
        return jsonify({"error": "Recipe not found"}), 404


# curl "http://127.0.0.1:5000/recipes"
@app.route('/recipes', methods=['POST']) # Action: Create
def create_recipe():
    # read json from the body
    json_data = request.json
    # Create the recipe using the DAO (this is a placeholder, implement as needed)
    new_recipe = recipe_dao.create(json_data['name'], json_data['ingredients', json_data['directions']])
    return jsonify(new_recipe), 201  # Return the created recipe with a 201 status code


@app.route('/recipes/<int:id>', methods=['PUT'])  # Action: Update
def update_recipe(id):
    # Read JSON data from the request body
    json_data = request.json

    # Check if the required fields are present
    if 'name' not in json_data or 'ingredients' not in json_data or 'directions' not in json_data:
        return jsonify({"error": "Invalid data, 'name', 'ingredients', and 'directions' are required."}), 400

    # Extract the data
    name = json_data['name']
    ingredients = json_data['ingredients']
    directions = json_data['directions']

    # Call the DAO to update the recipe
    updated_recipe = recipe_dao.update(id, name, ingredients, directions)

    if updated_recipe:
        # Return the updated recipe with a 200 status code
        return jsonify(updated_recipe), 200  
    else:
        # Return an error if the recipe was not found
        return jsonify({"error": "Recipe not found or update failed."}), 404  

@app.route('/recipes/<int:id>', methods=['DELETE'])  # Action: Delete
def delete_recipe(id):
    # Call the DAO to delete the recipe
    success = recipe_dao.delete(id)

    if success:
        # Return a success message with a 200 status code
        return jsonify({"message": "Recipe deleted successfully."}), 200
    else:
         # Return an error if the recipe was not found
        return jsonify({"error": "Recipe not found."}), 404 

if __name__ == "__main__":
    # Start the application (in debug mode)
    app.run(debug=True)