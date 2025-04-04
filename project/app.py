from flask import Flask, render_template, request


app = Flask(__name__, static_url_path='', static_folder='.') # Flask constructor
# makes static files accessible at the root URL (/) instead of /static

# Bind the index() funtion to the ‘/’ URL (homepage) 
@app.route('/')
def index():
    # Render the template 'index.html' from the 'templates' folder. render_template is good for dynamic content, so not using staticpages
    return render_template('index.html')

# curl "http://127.0.0.1:5000/recipies" 
@app.route('/recipies', methods=['GET']) # Action: Get All
def getall():
    return "\nget all\n"

# curl "http://127.0.0.1:5000/recipies/123"
@app.route('/recipies/<int:id>', methods=['GET']) # Action: Get. <int:id> is a variable, URL looks like ~/recipies/234
def findbyid(id):
    return "\nfind by id\n"

# curl "http://127.0.0.1:5000/recipies"
@app.route('/recipies', methods=['POST']) # Action: Create
def create():
    # read json from the body
    json_string = request.json
    return f"\ncreate {json_string}\n"

@app.route('/recipies/<int:id>', methods=['PUT']) # Action: Update
def update(id):
    json_string = request.json
    return f"\nupdate {id}{json_string}\n"

@app.route('/recipies/<int:id>d', methods=['DELETE']) # Action: Delete
def delete(id):
    return "\ndelete id\n"

if __name__ == "__main__":
    # Start the application (in debug mode)
    app.run(debug=True)