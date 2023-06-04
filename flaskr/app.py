from flask import Flask, render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField
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
  completed = db.Column(db.Boolean, unique=False, default=False)

# Todo form for adding items
class TodoForm(FlaskForm):
  todo = StringField("Todo")
  submit = SubmitField("Add")

@app.route('/', methods=["GET"])
def index():
    return render_template(
       'index.html',
        todos=Todo.query.all(),
        template_form=TodoForm()
        )

@app.route('/add', methods=["POST"])
def add():
    # if todo is filled in a POST request add it to the db
    if 'todo' in request.form:
      with app.app_context():
          db.session.add(
            Todo(
              todo_text=request.form['todo'],
              )
          )
          db.session.commit()
    return redirect('/')

@app.route('/update/<int:id>')
def update(id):
  # Let's take the id passed in the URL and toggle the done status
  with app.app_context():
      # Get the todo or return a 404
      todo = Todo.query.get_or_404(id)

      # Let's check if our todo is done or not:
      if todo.completed:
         todo.completed = False
      else:
         todo.completed = True

      # Ask the db to update the todo we got
      try:
        db.session.commit()
      except:
        return "Something went wrong with our db"
  return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
  # Let's take the id passed in the URL and try to delete the todo
  with app.app_context():
      # Get the todo or return a 404
      todo = Todo.query.get_or_404(id)

      # Ask the db to delete the todo we got
      try:
        db.session.delete(todo)
        db.session.commit()
      except:
        return "Something went wrong with our db"
  return redirect('/')