from app import app, db, Todo

# Create some sample todo's
todo_one = Todo(todo_text="Lean Python", todo_status="Open")
todo_two= Todo(todo_text="Lean Flas", todo_status="Open")
todo_three = Todo(todo_text="Create ToDo App", todo_status="Open")

# Create the inital DB
with app.app_context():
    db.create_all()

# Add the objects to a session
with app.app_context():
  db.session.add(todo_one)
  db.session.add(todo_two)
  db.session.add(todo_three)

# Write the session to the database
with app.app_context():
  db.session.commit