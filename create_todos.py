# FILE TO POPULATE DATABASE

from app import db, Todo

first_todo = Todo(todo_text = "learn Flask")
second_todo = Todo(todo_text = "setup venv")
third_todo = Todo(todo_text = "build a cool app")

db.session.add(first_todo)
db.session.add(second_todo)
db.session.add(third_todo)

db.session.commit()