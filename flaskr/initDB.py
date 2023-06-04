from app import app, db, Todo

# Create the inital DB
with app.app_context():
    db.create_all()

# Create some sample todo's
todo_one = Todo(todo_text="Learn Python", completed=False)
todo_two= Todo(todo_text="Learn Flask", completed=False)
todo_three = Todo(todo_text="Create ToDo App", completed=False)
todo_four= Todo(todo_text="Start Flask Server", completed=True)

# Add the objects to a session
with app.app_context():
  db.session.add(todo_one)
  db.session.add(todo_two)
  db.session.add(todo_three)
  db.session.add(todo_four)

  # Write the session to the database
  db.session.commit()
