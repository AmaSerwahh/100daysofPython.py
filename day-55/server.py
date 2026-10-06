from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def home():
    return ('<h1>Guess a number between 0 and 9</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3ZTh2NzRraGg5cTFheWVsdzhwZnBobGgxN3FvbHNjN3VjeXppdW5sbCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/wtkEOiGe9dppgDo7xQ/giphy.gif">')

number = random.randint(0,9)
print(number)
@app.route('/<int:num>')
def guess(num):
    if num == number:
        return (f'<h1 style="color:purple">{num} is just right.</h1><br>'
                f'<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWMyaXdzOTM1ZTI4dGo3eGhjMXo2eTNub2J0ZzY4eTNmajc0YXliYyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o7bu4G19uhzAf1DYQ/giphy.gif">')
    elif num > number:
        return (f'<h1 style="color:blue">{num} is too high.<br>'
                f'<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExM25vb2oxcWdtOW5uMTA0c2Iwb2JwdnFzemVwODByYjdoN3lzY2RjMyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/I1faV79waXwB34k4RS/giphy.gif">')
    else:
        return (f'<h1 style="color:red">{num} is too low.<br>'
                f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')


if __name__ == '__main__':
    app.run(debug=True)