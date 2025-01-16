from app.db import ( TodoModel, get_all_todos, get_engine,  )
from flask import ( Blueprint, flash, redirect, render_template, url_for )
from flask_wtf import ( FlaskForm )
from sqlalchemy.orm import ( Session )
from wtforms import ( StringField, SubmitField )
from wtforms.validators import ( DataRequired, Length )

todo_blueprint = Blueprint('main', __name__ )

class NewTodoForm(FlaskForm):
    description = StringField(
        'Todo Description',
        validators=[
            DataRequired(message="The todo item cannot be empty."),
            Length(min=4, message="The todo item must be at least 3 characters long."),
            # Regexp(r'^\S.*\S$|^\S$', message="The todo item cannot start or end with whitespace."),
        ]
    )
    submit = SubmitField('Add Todo')

@todo_blueprint.route("/", methods=['GET', 'POST'])
def index():
  # list of todos
  _todo_list = get_all_todos()
  
  # new todo WTF-Form
  new_todo_form = NewTodoForm()
  
  if new_todo_form.validate_on_submit():
    # get the contents of the todo
    _todo_description = new_todo_form.description.data
    
    # create new Todo item
    _todo = TodoModel(description=_todo_description)
    
    # save the todo
    _engine = get_engine()
    with Session(_engine) as session:
      session.add(_todo)
      session.commit()
      
      # flash success message
      flash("Task Added", "todo-added")
      
      # redirect to clear fields
      return redirect(url_for("main.index"))
    
  elif new_todo_form.errors:
    # flash all form validation errors for the fields
    for field, errors in new_todo_form.errors.items():
      for error in errors:
        flash(f"{error}", "error")

  return render_template("index.html", form=new_todo_form, todo_list=_todo_list )
