from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    results = data.json()
    return render_template("index.html", posts = results)

@app.route('/blog/post/<int:blog_id>')
def get_blog(blog_id):
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    results = data.json()

    ind_blog = results[blog_id - 1]
    return render_template("post.html", current_blog = ind_blog)

if __name__ == "__main__":
    app.run(debug=True)

