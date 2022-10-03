# IMPORT STATEMENTS FOR DEPENDENCIES
from flask import Flask, render_template, request, redirect
from models import db, Todo
from forms import CreateForm, UpdateForm, DeleteForm

# INSTANTIATE THE APP AS A FLASK OBJECT
app = Flask(__name__)

# SET DB CONFIGURATIONS AND SECRET KEY FOR SECURITY
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# @app.before_first_request
# def create_table():
#     db.create.all()

# app.run(host='localhost', port=3000)

# INDEX/GET ALL ROUTE
@app.route('/todos', methods=["GET", "POST"])
def index():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

# CREATE ROUTE
@app.route('/todos/create', methods=['GET', 'POST'])
def create_todo():
    if request.method == 'GET':
        return render_template('create.html', create_form=CreateForm())
    
    if request.method == 'POST':
        todo = Todo(todo_text=request.form['todo'])
        db.session.add(todo)
        db.session.commit()
        return redirect('/todos')

# UPDATE ROUTE
@app.route('/todos/<int:id>/update', methods=['GET', 'POST'])
def update_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    if request.method == 'POST':
        if todo:
            db.session.delete(todo)
            db.session.commit()

            todo_text = request.form['todo']
            todo = Todo(id=id, todo_text=todo_text)

            db.session.add(todo)
            db.session.commit()
            return redirect('/todos')
        return "To do item does not exist"
    return render_template('update.html', todo=todo, update_form=UpdateForm())

# DELETE ROUTE
@app.route('/todos/<int:id>/delete', methods=["GET", "POST"])
def deleteToDo(id):
    todo = Todo.query.filter_by(id=id).first()
    if request.method == "POST":
        if todo:
            db.session.delete(todo)
            db.session.commit()
            return redirect('/todos')
    return render_template('delete.html', delete_form=DeleteForm())