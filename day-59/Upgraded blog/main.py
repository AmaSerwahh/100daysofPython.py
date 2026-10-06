from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get('https://api.npoint.io/aeb423c2fe1acb912fb6')
    results = data.json()
    return render_template('index.html', results = results)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:blog_id>')
def get_blog(blog_id):
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    results = data.json()

    ind_blog = results[blog_id - 1]
    return render_template("post.html", current_blog = ind_blog)

if __name__ == '__main__':
    app.run(debug=True)
