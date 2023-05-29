from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SecretIndeed'

# Setting the path of the local db file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'

# Setting this to false to speed up things
app.config['SQLACLEMY_TRACK_MODIFICATIONS'] = False

# Connecting the DB to the app
db = SQLAlchemy(app)

# Todo class/model for holding todo's
class Todo(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  todo_text = db.Column(db.String(256), index = True)
  todo_status = db.Column(db.String(12), index = True)

# Todo form for adding items
class TodoForm(FlaskForm):
  todo = StringField("Todo")
  submit = SubmitField("Add")

@app.route('/')
def hello():
    return 'Hello, World!'
