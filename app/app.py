from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://chris:eldar911@localhost/flask-movie-dev'
app.debug =True
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<user %r> ' % self.username

@app.route('/')
def index():
    allUsers = User.query.all()
    for user in allUsers:
        print(user.id, user.username, user.email)
    return render_template('add_user.html')

@app.route('/post_user', methods=['POST'])
def post_user():
    username = request.form['username']
    email = request.form['email']
    user = User(username, email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()

