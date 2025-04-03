from flask import Flask, render_template

app = Flask(__name__, static_url_path='', static_folder='.') # Flask constructor
# makes static files accessible at the root URL (/) instead of /static

# Bind the index() funtion to the ‘/’ URL (homepage) 
@app.route('/')
def index():
    # Render the template 'index.html' from the 'templates' folder
    return render_template('index.html')



@app.route('/recipies', methods=['GET'])
def getall():
    return "get all"


if __name__ == "__main__":
    # Start the application (in debug mode)
    app.run(debug=True)