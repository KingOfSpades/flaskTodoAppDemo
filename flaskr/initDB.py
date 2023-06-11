from app import app, db, Todo

# Create the inital DB
with app.app_context():
    db.create_all()

# Create some sample todo's
todo_one = Todo(todo_text="Learn Python", completed=True)
todo_two = Todo(todo_text="Learn Flask", completed=True)
todo_three = Todo(todo_text="Create ToDo App", completed=True)
todo_four = Todo(todo_text="Start Flask Server", completed=True)
todo_five = Todo(todo_text="Add sorting to todo list", completed=False)
todo_six= Todo(todo_text="Add styling to todo list", completed=False)

# Add the objects to a session
with app.app_context():
  db.session.add(todo_one)
  db.session.add(todo_two)
  db.session.add(todo_three)
  db.session.add(todo_four)
  db.session.add(todo_five)
  db.session.add(todo_six)

  # Write the session to the database
  db.session.commit()
