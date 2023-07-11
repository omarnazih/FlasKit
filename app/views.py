from flask import render_template, request
from .models import Todo

from pony.orm import *
from . import app, db


@app.route('/')
@db_session
def index():
    todo_items = []    
    
    # Retrieve all Todo items from the database    
    todo_items = Todo.select()    
        
    print(todo_items)    
    return render_template('index.html', todo_items=todo_items)


# Define the route for creating new Todo items
@app.route('/todo', methods=['POST'])
@db_session
def create_todo():
    
    todo_item = Todo(title=request.form.get('title'), description=request.form.get('description'))
    db.commit()    

    context = {
     'todo_item': todo_item   
    }

    # Render a template with the updated list of Todo items
    return context