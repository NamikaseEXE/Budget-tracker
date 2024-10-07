from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# You can add more routes like this
@app.route('/about')
def about():
    return "<h1>About Page</h1>"

if __name__ == '__main__':
    app.run(debug=True)