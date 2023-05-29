from app import app, db, Todo

# Create the inital DB
with app.app_context():
    db.create_all()

# Create some sample todo's
todo_one = Todo(todo_text="Lean Python", todo_status="Open")
todo_two= Todo(todo_text="Lean Flask", todo_status="Open")
todo_three = Todo(todo_text="Create ToDo App", todo_status="Open")

# Add the objects to a session
with app.app_context():
  db.session.add(todo_one)
  db.session.add(todo_two)
  db.session.add(todo_three)

  # Write the session to the database
  db.session.commit()
