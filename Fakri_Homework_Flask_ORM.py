from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   email = db.Column(db.String(100))
   birthdate = db.Column(db.String(100))
   age = db.Column(db.Integer)

def __init__(self, name, email, birthdate, age):
   self.name = name
   self.email = email
   self.birthdate = birthdate
   self.age = age

@app.route('/')
def home():
   return render_template('home.html',  Users = Users.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['email'] or not request.form['birthdate'] or not request.form['age']:
         flash('Please enter all the fields', 'error')
      else:
         user = Users(name=request.form['name'], email=request.form['email'], birthdate=request.form['birthdate'], age=request.form['age'])
         
         db.session.add(user)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('home'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
