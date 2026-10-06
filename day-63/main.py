from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///all-books-collection.db"
db = SQLAlchemy(app)

class Book(db.Model):
    name = db.Column(db.String, primary_key=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == "POST":
        bookname = request.form['bookname']
        author = request.form['author']
        rating = request.form['rating']
        books = {
            'title': bookname,
            'author': author,
            'rating': rating
        }

        new_book = Book(name=bookname, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    return render_template('add.html')


@app.route("/edit/<title>", methods=['GET', 'POST'])
def edit(title):
    if request.method == "POST":
        book_to_update = Book.query.filter_by(name=title).first()
        book_to_update.rating = request.form['edit']
        db.session.commit()
        return redirect(url_for('home'))

    book_selected = Book.query.get(title)
    return render_template("edit.html", book=book_selected)


@app.route("/delete/<title>")
def delete(title):
    book_to_delete = Book.query.get(title)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)




