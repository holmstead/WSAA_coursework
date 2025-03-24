from flask import Flask, render_template

app = Flask(__name__) # Flask constructor

# Bind the index() funtion to the ‘/’ URL (homepage) 
@app.route('/')
def index():
    # Render the template 'index.html' from the 'templates' folder
    return render_template('index.html')

if __name__ == "__main__":
    # Start the application (in debug mode)
    app.run(debug=True)