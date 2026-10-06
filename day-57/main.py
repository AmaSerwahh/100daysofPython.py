from flask import Flask, render_template
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    name = 'Ama Serwah'
    return render_template('index.html', current_year=current_year, name=name)

@app.route('/guess/<some_name>')
def guess(some_name):
    data = requests.get(f"https://api.genderize.io?name={some_name}")
    results = data.json()
    gender = results['gender']

    data = requests.get(f"https://api.agify.io?name={some_name}")
    results = data.json()
    age = results['age']

    name = some_name.title()
    return render_template('guess.html', name=name, age=age, gender=gender)

@app.route('/blog')
def blog_page():
    data = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    results = data.json()
    return render_template('blog.html', posts = results)

if __name__ == '__main__':
    app.run(debug=True)

