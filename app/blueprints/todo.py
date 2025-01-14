from flask import ( Blueprint, render_template )

todo_blueprint = Blueprint('main', __name__ )

@todo_blueprint.get("/")
def index():
  return render_template("index.html")